import requests
import base64
import os
from dotenv import load_dotenv


# Load environment variables from .env file, this will try to load these values from your .env file
load_dotenv()

# Access the environment variables
s2s_oauth_client_secret = os.getenv("S2S_OAUTH_CLIENT_SECRET")
s2s_oauth_client_id = os.getenv("S2S_OAUTH_CLIENT_ID")
s2s_oauth_account_id = os.getenv("S2S_OAUTH_ACCOUNT_ID")
oauth_url = 'https://zoom.us/oauth/token?grant_type=account_credentials&account_id='+s2s_oauth_account_id  # Replace with your OAuth endpoint URL

def get_access_token():
    try:
        # Create the Basic Authentication header
        auth_header = f'Basic {base64.b64encode(f"{s2s_oauth_client_id}:{s2s_oauth_client_secret}".encode()).decode()}'

        # Define the headers for the OAuth request
        headers = {
            'Authorization': auth_header,
        }

        # Make the OAuth request
        response = requests.post(oauth_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response to get the access token
            oauth_response = response.json()
            access_token = oauth_response.get('access_token')
            return access_token
        else:
            print(f'OAuth Request Failed with Status Code: {response.status_code}')
            print(response.text)
            return None
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        return None


