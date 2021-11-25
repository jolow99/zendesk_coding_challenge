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

def format_ticket(ticket_number, tickets):
    # Return important ticket data
    return {
        "subject": tickets[ticket_number]["subject"],
        "description": tickets[ticket_number]["description"],
        "requester_id": tickets[ticket_number]["requester_id"],
        "status": tickets[ticket_number]["status"],
        "created_at": tickets[ticket_number]["created_at"],
    }
     
