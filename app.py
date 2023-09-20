from flask import Flask, render_template, jsonify, request
from S2SOAuth import get_access_token
from webhook import handle_request
import requests

app = Flask(__name__)

# Define a route for the web page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the web service
@app.route('/api/data', methods=['GET'])
def api_data():
    # Simulate some data
    data = {'message': 'Hello, world!', 'value': 42}
    return jsonify(data)

# Define a route for the web service
@app.route('/GetAccessToken', methods=['GET'])
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
    return 'This is a GET request to webhook.py', 200

if __name__ == '__main__':
    app.run(debug=True)