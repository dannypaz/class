#!/usr/bin/env python
# http://mrjob.readthedocs.io/en/latest/guides/writing-mrjobs.html#multi-step-jobs
from mrjob.job import MRJob
from mrjob.step import MRStep
import json
from collections import Counter
from collections import defaultdict


class MRMostUsedWord(MRJob):

    def mapper_get_words(self, _, line):
        """Take in stdin and return each hashtag with the number one"""

        for tweet in line.split('/n'):
            try:
                entity = json.loads(tweet)
                try:
                    entity = entity['entities']
                    if entity is not None and (entity['hashtags'] is not None
                                            or len(entity['hashtags']) != 0):
                        for hashtags in entity['hashtags']:
                            yield(hashtags['text'].lower().encode('utf-8'), 1)
                    else:
                        pass
                except KeyError:
                    continue
            except ValueError:
                continue

    def combiner_count_words(self, word, counts):
        """sum the hashtags we've seen so far"""
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        """send all (num_occurrences, word) pairs to the same reducer
        with a null key"""
        yield None, (sum(counts), word)

    def reducer_find_top_hashtags(self, _, word_count_pairs):
        """ return the top ten hashtags from the word_count_pairs generator"""
        top_hashtags = defaultdict(int)
        for hashtag_number in list(word_count_pairs):
            top_hashtags[hashtag_number[1].encode('utf-8')] += hashtag_number[0]
        print(top_hashtags)
        for hash_t, num in Counter(top_hashtags).most_common(20):
            print("{}\t{}".format(hash_t, num))

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_top_hashtags)
        ]


if __name__ == '__main__':
    MRMostUsedWord.run()
