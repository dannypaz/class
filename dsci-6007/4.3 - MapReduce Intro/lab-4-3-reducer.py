#!/usr/bin/env python
import sys
from functools import reduce
from collections import Counter


def reducer():
    """Input: stdin or hastag and number.
     Output: hastag followed by number of times hastag occurs."""

    current_hashtag = ''
    running_total = 0
    for line in sys.stdin:
        for hashtag in line.strip().split('/t', 1):
            try:
                int(hashtag)
                continue
            except ValueError:
                if len(hashtag) > 1:
                    if running_total == 0:
                        current_hashtag = hashtag
                        running_total += 1
                    elif hashtag != current_hashtag:
                        print("{}\t{}".format(current_hashtag, running_total))
                        running_total = 0
                        current_hashtag = hashtag
                        running_total += 1
                    else:
                        running_total += 1
                else:
                    continue


if __name__ == "__main__":
    reducer()
