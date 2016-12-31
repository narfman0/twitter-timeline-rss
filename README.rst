====================
twitter-timeline-rss
====================

.. image:: https://img.shields.io/pypi/v/twitter-timeline-rss.svg
        :target: https://pypi.python.org/pypi/twitter-timeline-rss

.. image:: https://img.shields.io/travis/narfman0/twitter-timeline-rss.svg
        :target: https://travis-ci.org/narfman0/twitter-timeline-rss

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

CLI
---

The command line interface may be used to dump your timeline to stdout::

    twitter_timeline_rss

An arbitrary user may be dumped with `--user`::

    twitter_timeline_rss --user narfman0

or it may be directed at a file with `--file`::

    twitter_timeline_rss --user narfman0 --file narfman0.atom

License
=======

Copyright (c) 2016 Jon Robison

See included LICENSE for licensing information
