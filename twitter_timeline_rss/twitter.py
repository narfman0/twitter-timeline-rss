""" Entry point for web app """
import tweepy
from flask import Flask
from twitter_timeline_rss import settings
from werkzeug.contrib.atom import AtomFeed


app = Flask(__name__)
auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


@app.route('/<username>')
def feed(username):
    title = "{}'s timeline".format(username)
    feed = AtomFeed(title, feed_url='/', url='/', subtitle="twitter-timeline-rss for now")
    public_tweets = api.user_timeline(username)
    for tweet in public_tweets:
        feed.add(tweet.title, tweet.text, content_type='html',
                 author=tweet.author.screen_name, url=tweet.source_url, id=tweet.id,
                 published=tweet.created_at)
    return feed.get_response()
