import os
import sys
from datetime import datetime

# Adds the parent directory to the path to import existing modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def lambda_handler(event, context):
    print(f"Starting Raw to Staging ETL - {datetime.now()}")
    
    # Checks if it's a manual or scheduled execution
    execution_type = event.get('execution_type', 'manual')
    print(f"Execution type: {execution_type}")
    
    try:
        from scripts.run_raw_to_staging import main
        main()
        return {
            'statusCode': 200,
            'body': 'Raw to Staging ETL executed successfully!'
        }
    except Exception as e:
        print(f"Error during ETL: {str(e)}")
        raise e