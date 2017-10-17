#!/usr/bin/env python
# http://mrjob.readthedocs.io/en/latest/guides/writing-mrjobs.html#multi-step-jobs
from mrjob.job import MRJob
from string import punctuation
import json


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        """Creater a counter using MrJobs built in counter function."""
        for word in line.split():
            self.increment_counter("word", word.strip(punctuation).lower())

        for tweet in line.split('/n'):
            try:
                entity = json.loads(tweet)
                try:
                    entity = entity['entities']
                    if entity is not None and (entity['hashtags'] is not None
                            or len(entity['hashtags']) != 0):
                        for hashtags in entity['hashtags']:
                            self.increment_counter("hashtag",
                            hashtags['text'].lower().encode('utf-8'))
                    else:
                        pass
                except KeyError:
                    continue
            except ValueError:
                continue


if __name__ == '__main__':
    MRWordFreqCount.run()
