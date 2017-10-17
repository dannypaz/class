#!/usr/bin/env python

import json
import sys

for line in sys.stdin:
    line = line.strip()
    tweet = json.loads(line)
    entities = tweet.get('entities')
    if entities:
        for hashtag in entities.get('hashtags', []):
            try:
                print '%s\t%s' % (hashtag.get('text'), 1)
            except UnicodeEncodeError:
                pass
