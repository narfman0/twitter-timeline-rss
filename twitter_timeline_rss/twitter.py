""" Entry point for web app """
from datetime import datetime
import tweepy
from flask import Flask
from werkzeug.contrib.atom import AtomFeed
from twitter_timeline_rss import settings


app = Flask(__name__)
auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY,
                           settings.TWITTER_CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN,
                      settings.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


@app.route('/')
def home():
    return generate_response(api.me().screen_name, api.home_timeline())


@app.route('/<username>')
def feed(username):
    return generate_response(username, api.user_timeline(username))


def generate_response(username, tweets):
    title = "@{}'s twitter timeline".format(username)
    subtitle = 'Timeline as of {date}'.format(date=datetime.now())
    feed = AtomFeed(title, feed_url='/', url='/', subtitle=subtitle)
    for tweet in tweets:
        tweet_title = "@{}'s tweet from: {}".format(tweet.author.screen_name,
                                                    tweet.created_at.__str__())
        feed.add(tweet_title, tweet.text, content_type='html',
                 author=tweet.author.screen_name, url=tweet.source_url,
                 id=tweet.id, published=tweet.created_at,
                 updated=tweet.created_at)
    return feed.get_response()
