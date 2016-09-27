====================
twitter-timeline-rss
====================

Ingest a twitter timeline and render as RSS. This python web app is a service
to ingest arbitrary user's timelines as rss feeds, so you don't have to go
to twitter manually to read through quips and witticisms. Takes username as
parameter for any timeline.

Usage
=====

Optional: set up virtualenv environment with::

    virtualenv venv
    source venv/bin/activate

Install requirements::

    pip install -r requirements.txt

Change directory into twitter_timeline_rss and run flask server::

    cd twitter_timeline_rss
    FLASK_APP=twitter.py flask run

Hit the endpoint with something like this url in your favorite browser::

    http://127.0.0.1:5000/narfman0

License
=======

Copyright (c) 2016 Jon Robison

See included LICENSE for licensing information
