import pandas as pd
import boto3
import io
import re
import pyarrow as pa
import pyarrow.parquet as pq
from config import settings
from config.settings import secrets
from .modules import tracks_raw_to_staging, album_raw_to_staging, artist_raw_to_staging

# Main function to orchestrate the ETL from raw to staging
def run_etl_raw_to_staging():

  """
  Reads raw CSV files from an S3 bucket, applies transformation functions
  (by module), converts the data to Parquet format, and uploads it to the staging path in S3.
  """
   
  # ** Client S3 **
  s3_client = boto3.client(
    "s3",
    aws_access_key_id=secrets["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=secrets["AWS_SECRET_ACCESS_KEY"]
)

  # Mapping of file keywords to processing functions
  list_of_modules = {
    'tracks': tracks_raw_to_staging.tracks_process,
    'album' : album_raw_to_staging.album_process,
    'artist': artist_raw_to_staging.artist_process
      }

  # Lists objects in the raw data folder
  response = s3_client.list_objects_v2( Bucket=settings.bucket_name, Prefix=settings.raw_path)

  # Loop through each CSV file found in S3
  for obj in response['Contents']:
    if(obj['Key'].endswith('.csv')):
      object = s3_client.get_object(Bucket=settings.bucket_name, Key=obj['Key'])
      df = pd.read_csv(io.BytesIO(object['Body'].read())) 
      file_name= obj['Key'].split('/')[-1]

      print(f"Processing the File Name: {file_name}")
    
      # Identifies the correct module for processing based on the file name
      for key in list_of_modules:
        if key in file_name.lower():
            module = list_of_modules[key]
            df = module(df)

      print(df.head()) # Preview of the processed DataFrame

      # Converts DataFrame to Parquet table
      table = pa.Table.from_pandas(df)
      buffer = io.BytesIO()
      pq.write_table(table, buffer)
      buffer.seek(0)

      print(df.info()) # Check the current data types

      # Cleans the file name and uploads to the staging folder in S3
      clean_the_currently_file_name = file_name.replace(file_name, re.sub(r'\_2023.csv', '', file_name))
      new_file_name = f"{clean_the_currently_file_name}.parquet"
      key_s3_parquet = settings.staging_path + new_file_name

      # Final Process: Upload the Parquet file to S3
      s3_client.put_object(Bucket=settings.bucket_name, Key=key_s3_parquet, Body=buffer.getvalue())
  
  print('ETL process completed successfully!')