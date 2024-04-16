from flask import Flask, render_template, jsonify, request
from meetingsdk import handle_meetingsdk
from s2soauth import get_access_token
from webhook import handle_request
from redirectforoauth import handle_redirect_url_data_request
from oauthrefreshtoken import handle_oauth_refresh_token_data_request


import requests
import os
from dotenv import load_dotenv


# Load environment variables from .env file, this will try to load these values from your .env file
load_dotenv()

app = Flask(__name__)

# Define a route for the web page
@app.route('/')
def index():
    return render_template('index.html')


# Define a route for the web service
@app.route('/s2soauthaccesstoken', methods=['GET'])
def GetAccessToken():
    access_token = get_access_token()
    if access_token:
        print(f'Access Token: {access_token}')
        return jsonify(access_token)
    else:
        print('Failed to retrieve an access token.')

# Define a route to handle POST requests
@app.route('/webhook', methods=['POST'])
def handle_post_webhook():
    # You can handle POST requests here
    # The request data can be accessed using request.json or request.form
    # Perform your webhook processing logic
    response=handle_request(request)
    
    return response

# Define a route to handle GET requests
@app.route('/webhook', methods=['GET'])
def handle_get_webhook():
    # You can handle GET requests here
    # Perform your GET webhook processing logic
    
    # For example, return a response for GET requests
    response=handle_request(request)
    
    return response



# Define a route to handle POST requests
@app.route('/redirecturlforoauth', methods=['GET'])
def handle_get_oauth():
    oauth_client_secret = os.getenv("OAUTH_CLIENT_SECRET")
    oauth_client_id = os.getenv("OAUTH_CLIENT_ID")

    # Get the value of the 'code' query string parameter
    code = request.args.get('code')
    
    # You can handle POST requests here
    # The request data can be accessed using request.json or request.form
    # Perform your webhook processing logic
    response=handle_redirect_url_data_request("redirecturlforoauth",oauth_client_id,oauth_client_secret,code)
    if response:
        return response
    else:
        print('Failed to retrieve an access token.')   
    return response

# Define a route to handle POST requests
@app.route('/oauthrefreshtoken', methods=['GET'])
def handle_get_oauth_refresh_token():
    oauth_client_secret = os.getenv("OAUTH_CLIENT_SECRET")
    oauth_client_id = os.getenv("OAUTH_CLIENT_ID")

    # Get the value of the 'code' query string parameter
    refreshtoken = request.args.get('refreshtoken')
    
    # You can handle POST requests here
    # The request data can be accessed using request.json or request.form
    # Perform your webhook processing logic
    response=handle_oauth_refresh_token_data_request(oauth_client_id,oauth_client_secret,refreshtoken)
    if response:
        return response
    else:
        print('Failed to retrieve an access token.')   
    return response

# Define a route to handle POST requests
@app.route('/meetingsdk', methods=['GET'])
def handle_get_meetingsdk():
    msdk_client_secret = os.getenv("MSDK_CLIENT_SECRET")
    msdk_client_id = os.getenv("MSDK_CLIENT_ID")

    # Get the value of the 'code' query string parameter
    refreshtoken = request.args.get('refreshtoken')
    
    # You can handle POST requests here
    # The request data can be accessed using request.json or request.form
    # Perform your webhook processing logic
    response=handle_meetingsdk(msdk_client_id,msdk_client_secret)
    if response:
        return response
    else:
        print('Failed to retrieve an access token.')   
    return response

if __name__ == '__main__':
    app.run(debug=True)