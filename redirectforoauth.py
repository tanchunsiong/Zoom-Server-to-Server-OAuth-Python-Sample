from flask import Flask, request, jsonify
import base64
import requests
import urllib.parse  # Import the urllib module for URL encoding

def handle_redirect_url_data_request(path, oauth_client_id, oauth_client_secret, code):
    print ("handle_redirect_url_data_request")
    url = f"https://zoom.us/oauth/token"
    redirect_uri=f"https://python.asdc.cc/{path}"
    print (redirect_uri)
    
    # Encode the client ID and client secret
    (credentials) = f"{oauth_client_id}:{oauth_client_secret}"
    credentials_encoded = base64.b64encode(credentials.encode()).decode('utf-8')

    headers = {
        'Authorization': f'Basic {credentials_encoded}',
        'Content-Type': 'application/x-www-form-urlencoded',
       
    }
    print (credentials_encoded)

    data = {
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        'code': code
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


