import json
import hashlib
import hmac
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv


# Load environment variables from .env file, this will try to load these values from your .env file
load_dotenv()




oauth_secret_token = os.getenv("OAUTH_SECRET_TOKEN")

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
                    oauth_secret_token.encode('utf-8'),
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
            message = "Success."
            
            # Save the POST body to a text file
            with open('webhook.txt', 'w') as file:
                file.write(str(request.get_json()))

            return message, 200

    elif request.method == 'GET':
        # This block handles GET requests

        # Read the content of the text file
        try:
            with open('webhook.txt', 'r') as file:
                file_content = file.read()
            return file_content, 200
        except FileNotFoundError:
            return "File not found.", 404

    else:
        # Unsupported HTTP method
        return "Unsupported HTTP method.", 405
