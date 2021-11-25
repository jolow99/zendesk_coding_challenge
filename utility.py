import requests
import json

with open('config.json') as config:
    config = json.load(config)
subdomain = config['subdomain']
auth = config['authentication']

def get_tickets():
    url = f"https://{subdomain}.zendesk.com/api/v2/requests/open.json"
    headers = {
    # 'Content-Type': 'application/json',
    'Authorization': f'Basic {auth}',
    }
    response = requests.request("GET", url, headers=headers)
    return json.dumps(response.json()["requests"], indent=4)