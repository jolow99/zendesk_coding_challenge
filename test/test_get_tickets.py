import json 
import requests

with open('config.json') as config:
    config = json.load(config)
subdomain = config['subdomain']
auth = config['authentication']

def test_get_tickets_check_status_code_equals_200(): 
    url = f"https://{subdomain}.zendesk.com/api/v2/requests/open.json"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {auth}',
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200

def test_get_tickets_check_content_type_equals_json():
    url = f"https://{subdomain}.zendesk.com/api/v2/requests/open.json"
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {auth}',
    }
    response = requests.request("GET", url, headers=headers)
    assert response.headers["Content-Type"] == "application/json; charset=UTF-8"

