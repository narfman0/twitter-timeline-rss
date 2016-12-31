#!/usr/bin/env python
import argparse

from twitter_timeline_rss.twitter import feed, home


parser = argparse.ArgumentParser(description='Dump twitter RSS feeds')
parser.add_argument('--user', help='User from which to ingest timeline')
parser.add_argument('--file', help='Dump to specified file instead of stdout')
args = parser.parse_args()


def main():
    response_object = feed(args.user) if args.user else home()
    response_text = response_object.response
    if isinstance(response_text, list):
        response_text = b''.join(response_text)
    if args.file:
        with open(args.file, 'w') as f:
            f.write(response_text)
    else:
        print(response_text)
