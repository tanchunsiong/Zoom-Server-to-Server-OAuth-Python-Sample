This is a sample code to demonstrate how to call Zoom S2S OAuth using Python and Flask


The main logic of this sample is in app.py

This demo still require python and `pip3 install flask`,`pip install requests` and `pip install python-dotenv`

You will also need a .env in the root directory with these values

# Your .env file should look something like this

S2S_OAUTH_CLIENT_ID=''
S2S_OAUTH_CLIENT_SECRET=''
S2S_OAUTH_ACCOUNT_ID=''
OAUTH_SECRET_TOKEN=''
OAUTH_CLIENT_ID=''
OAUTH_CLIENT_SECRET=''
MSDK_CLIENT_SECRET=''
MSDK_CLIENT_ID=''


The index.html file contains a simple webpage with an empty <div> element where data from the web service will be displayed using JavaScript's fetch function.

To run this code, make sure you have Flask installed. You can install it using pip install Flask. Run it via `python3 app.py`. The web server will start, and you can access the web page at http://localhost:5000/.

When you visit the web page, it will display the message from the web service, which is fetched using JavaScript. The web service is accessible at http://localhost:5000/api/data.
