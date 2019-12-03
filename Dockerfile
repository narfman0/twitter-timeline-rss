FROM python:alpine

RUN pip install twitter-timeline-rss

CMD ["twitter_timeline_rss"]
