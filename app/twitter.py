import os
from os.path import join, dirname
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

session = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)


def tweet(status):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    resp = session.post(url, {'status': status})

    return resp
