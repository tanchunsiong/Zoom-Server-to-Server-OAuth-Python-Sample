import json
import hashlib
import hmac
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv


# Load environment variables from .env file, this will try to load these values from your .env file
load_dotenv()


# Your .env file should look something like this

#CLIENT_ID='xxxxxxxxxx'
#CLIENT_SECRET='yyyyyyyyyyyyy'
#ACCOUNT_ID='zzzzzzzzzzzz'
#secret_token='123412341234123'

secret_token = os.getenv("secret_token")

app = Flask(__name__)

def handle_request(request):

    if request.method == 'POST':
        # This block handles POST requests

        # Get the raw POST data from the request
        input_data = request.data

        # Decode the JSON data
        try:
            data = json.loads(input_data)
        except json.JSONDecodeError:
            return "Invalid JSON data", 400

        # Check if the event type is "endpoint.url_validation"
        if data.get('event') == 'endpoint.url_validation':
            # Check if the payload contains the "plainToken" property
            payload = data.get('payload', {})
            plain_token = payload.get('plainToken')
            if plain_token is not None:
                # Hash the plainToken using HMAC-SHA256
                encrypted_token = hmac.new(
                    secret_token.encode('utf-8'),
                    plain_token.encode('utf-8'),
                    hashlib.sha256
                ).hexdigest()

                # Create the response JSON object
                response = {
                    "plainToken": plain_token,
                    "encryptedToken": encrypted_token
                }

                # Set the response content type to JSON
                return response, 200
            else:
                # Payload is missing the "plainToken" property
                return "Payload is missing 'plainToken' property.", 400
        else:
            # Invalid event type
            return "Invalid event type.", 400

    elif request.method == 'GET':
        # This block handles GET requests

        # Handle your GET request logic here

        # For example, you can retrieve query parameters using request.args
        param1 = request.args.get('param1')
        if param1 is not None:
            return f"Received GET request with param1 = {param1}"
        else:
            return "Received GET request without param1"

    else:
        # Unsupported HTTP method
        return "Unsupported HTTP method.", 405
