#Preciso reconstruir para straging to Analytics
import pandas as pd
import boto3
import io
import os
import pyarrow as pa
import pyarrow.parquet as pq
from config import settings
from config.settings import secrets

# Main function to perform ETL from staging to analytics
def run_etl_staging_to_analytics():

        """
        Reads Parquet files from the staging folder in S3, performs joins to create
        an analytics-ready dataset, and uploads the final Parquet file to the analytics path in S3.
        """
        # Initialize S3 client
        s3_client = boto3.client(
           "s3",
            aws_access_key_id=secrets["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=secrets["AWS_SECRET_ACCESS_KEY"]
        )

        # Dictionary to store loaded DataFrames
        dataframes = {}

        # List files in the staging folder
        response = s3_client.list_objects_v2( Bucket=settings.bucket_name, Prefix=settings.staging_path)

        # Read each Parquet file and assign to corresponding variable
        for obj in response['Contents']:
            if(obj['Key'].endswith('.parquet')):
                object = s3_client.get_object(Bucket=settings.bucket_name, Key=obj['Key'])
                df = pd.read_parquet(io.BytesIO(object['Body'].read())) 
                file_name= obj['Key'].split('/')[-1].lower().strip()

                print(f"Processing the File Name: {file_name}")

                if 'album' in file_name:
                        dataframes['album'] = df
                elif 'artist' in file_name:
                        dataframes['artist'] = df
                elif 'tracks' in file_name:
                        dataframes['tracks'] = df

        print(f'DataFrame Keys',dataframes.keys())

        # Validate all required DataFrames are present
        expected_keys = ['album', 'artist', 'tracks']

        if all(key in dataframes for key in expected_keys):
                df_album = dataframes['album']
                df_artist = dataframes['artist']
                df_tracks = dataframes['tracks'] 
        else:
                print('One of more DataFrame are missing!')  

        # Perform joins to build final Analytics dataset
        df_ambum_artist = pd.merge(df_album, df_artist, left_on='artist_id', right_on='id')

        df_track_ambum_artist = pd.merge(df_tracks, df_ambum_artist, left_on='id', right_on='track_id')

        # Analyzing the columns after join
        print(f'Columns after join:', df_track_ambum_artist.columns.tolist()) 
        # ** Analyzing the Data Types
        print(f'Data types after join:', df_track_ambum_artist.info())

        # Drop redundant ID columns
        df_track_ambum_artist = df_track_ambum_artist.drop(columns=['id_x', 'id_y'])

        print(f'Final DataFrame columns after cleanUp:',df_track_ambum_artist.columns.tolist())

        # Convert final DataFrame to Parquet and upload to S3
        table = pa.Table.from_pandas(df_track_ambum_artist)
        buffer = io.BytesIO()
        pq.write_table(table, buffer)
        buffer.seek(0)

        #Rename the file and upload it to S3
        output_file_name = 'sportify_analysis.parquet'
        key_s3_parquet = settings.analytics_path + output_file_name

        s3_client.put_object(Bucket=settings.bucket_name, Key=key_s3_parquet, Body=buffer.getvalue())

        print(f'The file {output_file_name} successfully uploaded to S3 at: {key_s3_parquet}')