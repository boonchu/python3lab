

The code from this video can be found here.

IMPORTANT: Depending on the version of Flask you have, you may or may not be able to store a credentials object in the login_session the same way that Lorenzo does. You may get the following error:

OAuth2Credentials object is not JSON serializable

What should you do to fix this? There are three options:

    Rather than storing the entire credentials object you can store just the access token instead. It can be accessed using credentials.access_token.
    The OAuth2Credentials class comes with methods that can help you. The .to_json() and .from_json() methods can help you store and retrieve the credentials object in json format.
    Update your versions of Flask, _ and _ to match Lorenzo's. Use the following commands:

```
pip install werkzeug==0.8.3
pip install flask==0.9
pip install Flask-Login==0.1.3
```

Note: If you get a permissions error, you will need to include sudo at the beginning of each command. That should look like this: sudo pip install flask==0.9

Go to the GoogleDevConsole> API & Auth> Credentials>Select your app> Authorized Redirect URIs and add the following URIS: http://localhost:5000/login and http://localhost:5000/gconnect You may have to change the port number depending on the port number you have set your app to run on.

