import requests
import json
import threading

with open('config.json') as config:
    config = json.load(config)
subdomain = config['subdomain']
auth = config['authentication']

def get_tickets():
    url = f"https://{subdomain}.zendesk.com/api/v2/requests/open.json"
    headers = {
    'Content-Type': 'application/json',
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

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, *init_args, **init_kwargs):
        threading.Thread.__init__(self, *init_args, **init_kwargs)
        self._return = None
    def run(self):
        self._return = self._target(*self._args, **self._kwargs)
    def join(self):
        threading.Thread.join(self)
        return self._return
     
