from flask import Flask, render_template, jsonify, request
from S2SOAuth import get_access_token

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


if __name__ == '__main__':
    app.run(debug=True)