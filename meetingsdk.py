from flask import Flask, jsonify
import jwt
import hashlib
import hmac
import base64
import time
import datetime

#pip3 install PyJ

app = Flask(__name__)

def generate_signature(data, secret):
    encoded_jwt = jwt.encode(data, secret, algorithm="HS256")
    return encoded_jwt

@app.route('/')
def handle_meetingsdk(msdk_client_id, msdk_client_secret):
    epoch_time = int(time.time())
    epoch_time_48hours_later = epoch_time + 172800
    SDK_SECRET = msdk_client_secret
    APP_KEY = msdk_client_id
    data = {
        "appKey": APP_KEY,
        "iat": epoch_time,
        "exp": epoch_time_48hours_later,
        "tokenExp": epoch_time_48hours_later,
        "mn": 9898533313,
        "role": 1
    }
    meeting_sdk_key = generate_signature(data, SDK_SECRET)

    # Get the current date
    current_date = datetime.date.today()

    # Create a datetime object for the start of the day
    start_of_day = datetime.datetime.combine(current_date, datetime.time.min)

    # Get the epoch time (in seconds) for the start of the day
    epoch_time = int(start_of_day.timestamp())

    epoch_time_48hours_later = epoch_time + 172800
    data = {
        "appKey": APP_KEY,
        "iat": epoch_time,
        "exp": epoch_time_48hours_later,
        "tokenExp": epoch_time_48hours_later,
        "mn": 9898533313,
        "role": 1
    }
    meeting_sdk_key_control = generate_signature(data, SDK_SECRET)

    return jsonify({"Meeting SDK Key": meeting_sdk_key, "Meeting SDK Key - Control": meeting_sdk_key_control})
