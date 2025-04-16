# *** Settings.py *** #
from pathlib import Path
import os
import json
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

def get_aws_secret():

    secret_name = "spotify-etl-secrets"
    region_name = "ca-central-1"

    try:
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response['SecretString'])
    except ClientError as e:
        print(f"Error fetching AWS secrets: {e}")
        return None

# Load variables (AWS Secrets Manager -> Fallback to .env)
secrets = get_aws_secret()

if secrets:
    # Set environment variables
    for key, value in secrets.items():
        os.environ[key] = value
else:
    # Fallback to local development
    env_path = Path(__file__).resolve().parent.parent / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
    else:
        raise EnvironmentError("No configuration found (AWS Secrets Manager or .env)")

# Project variables (now accessible via os.environ)
bucket_name = os.getenv('bucket_name')
raw_path = os.getenv('raw_path')
staging_path = os.getenv('staging_path')
analytics_path = os.getenv('analytics_path')