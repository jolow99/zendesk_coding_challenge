import json 
import requests

with open('create_tickets/tickets.json') as tickets, open('config.json') as config:
    tickets = json.load(tickets)
    config = json.load(config)

subdomain = config['subdomain']
auth = config['authentication']

url = f"https://{subdomain}.zendesk.com/api/v2/imports/tickets/create_many.json"
payload=json.dumps(tickets)
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Basic {auth}',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)