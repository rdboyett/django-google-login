import os
ROOT_PATH = os.path.dirname(__file__)

#place your goole client_secrects.json download in the same directory as this file.
CLIENT_SECRETS = os.path.join(ROOT_PATH,'..', 'client_secrets.json')

#Add any scopes that you want access to in the credentials file
SCOPES = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    # Add other requested scopes.
]

#Change the redirect uri for your project
redirect_uri='http://127.0.0.1:8000/google/oauth2callback'

#Login Success redirect
LOGIN_SUCCESS = '/google/success/'

#change to any random hashed sequence
SECRET_KEY = 't(641aasfrv6^^-1sj$uzq(fskmd%+!33199$axb1hu(2i_2n='

#make sure this email is matched up to the project email settings.py
WEBMASTER_EMAIL = 'rdboyett@gmail.com'

WEBSITENAME = 'YOUR WEBSITE NAME'

ROOT_WEBSITE_LINK = 'http://127.0.0.1:8000'
