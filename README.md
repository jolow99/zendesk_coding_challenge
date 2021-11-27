# Zendesk Ticket Viewer Documentation

## Installation 

```
https://github.com/jolow99/zendesk_coding_challenge.git
```
Open a terminal and type:
```
cd zendesk_coding_challenge
pip install pytest
```

To set up authentication, create a file called `config.py` in the root folder with the following contents:
```
{
"subdomain": "<Subddomain>",
"authentication": "<Base64 encoded username and password>"
}
```
To get the base64 encoded username and password, you can use the auth.py helper function
Go into auth.py, replace the username and password, run the file, and copy the output
## Usage 
Once authentication has been set up, to run the CLI application, ensure you are in the root directory of the project and type
```
python3 main.py
```
