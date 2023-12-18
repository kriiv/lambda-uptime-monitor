import json
import requests
import os

def lambda_handler(event, context):
    # List of endpoints to check
    urls_to_check = ["https://example.com", "https://example.com"]

    # Slack webhook URL
    slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']

    for url in urls_to_check:
        try:
            response = requests.get(url)
            
            # Check if status code is not 200
            if response.status_code != 200:
                # Prepare message
                message = {
                    "text": f"Alert! The endpoint {url} returned status code {response.status_code}"
                }
                # Send message to Slack
                requests.post(slack_webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
        
        except requests.RequestException as e:
            print(f"Error checking {url}: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Function executed successfully!')
    }
 
