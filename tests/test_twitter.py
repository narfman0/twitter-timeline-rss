#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
import unittest

from twitter_timeline_rss.twitter import generate_response


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class TestTwitterTimelineRSS(unittest.TestCase):
    def setUp(self):
        self.tweet = AttrDict({
            'author': AttrDict({'screen_name': 'screen_name1'}),
            'created_at': datetime.now(),
            'source_url': 'url1',
            'id': 1,
            'text': 'text1',
        })

    def test_generate_response(self):
        response = generate_response('narfman0', [self.tweet])
        self.assertEquals(response.status_code, 200)
