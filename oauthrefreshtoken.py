from flask import Flask, request, jsonify
import base64
import requests
import urllib.parse  # Import the urllib module for URL encoding

def handle_oauth_refresh_token_data_request(oauth_client_id, oauth_client_secret, code):
    print ("handle_oauth_refresh_token_data_request")
    url = f"https://zoom.us/oauth/token"
    
    # Encode the client ID and client secret
    credentials = f"{oauth_client_id}:{oauth_client_secret}"
    credentials_encoded = base64.b64encode(credentials.encode()).decode('utf-8')

    headers = {
        'Authorization': f'Basic {credentials_encoded}',
        'Content-Type': 'application/x-www-form-urlencoded',
       
    }
    print (credentials_encoded)

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': code
    }
    # Encode the data dictionary as x-www-form-urlencoded
    data_encoded = urllib.parse.urlencode(data).encode('utf-8')


    response = requests.post(url, data=data_encoded, headers=headers)
    # Check the HTTP status code before parsing as JSON
    if response.status_code == 200:
       print ("response 200")
       response_json = response.json()
       print(response_json)
       return response_json, 200  # Return JSON response with 200 status code
    else:
        
        # Handle the case where the response has an error status code
        return "Error: " + str(response.status_code), response.status_code


