#!/usr/bin/env python
import sys
from functools import reduce
from collections import Counter
from collections import defaultdict


def reducer():
    """Input: stdin or hastag and number of times it occurs.
     Output: hastag followed by number of times hastag occurs ranked
     by frequency."""
    top_hashtags = defaultdict(int)
    current_hashtag = ''
    for line in sys.stdin:
        for hashtag_number in line.strip().split('/t'):
            try:
                int(hashtag_number)  # this is the number
                hashtag_number = int(hashtag_number)
                top_hashtags[current_hashtag] += hashtag_number
            except ValueError:
                if len(hashtag_number) > 1:
                    current_hashtag = hashtag_number
    for hash_t, num in Counter(top_hashtags).most_common(20):
        print("{}\t{}".format(hash_t, num))


if __name__ == "__main__":
    reducer()
