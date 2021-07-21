# Import packages
import pip
import tweepy
import time


# Authenticate to twitter

consumer_key = '9YdZXi265LOxSy7lqvKghdd0g'
consumer_secret = 'rniMYrCTQ9BBsGXCLGWZ9CWBIppNhXojrYA17sUwvTe2mjPBSp'
access_key = '1417196890593140736-roFfvq4v1fYWsoTzT44kOUC9vBjMqO'
access_secret = 'Uc43oEuMqgy6oUb6GzokjetbksD6yceTgY4Z7m19eAHSo'


# Create API object

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)

user = api.me()
search = 'breastcancer'
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    try:
        tweet.retweet()
        print("Retweet")
        time.sleep(0)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
