#!/usr/bin/python3 -u

import sys
import re
from collections import defaultdict

# Regular expression defining the word delimiter
delimRegEx = '[\s\.,;!?\*\^\(\)\[\]\{\}]'

# Create dictionary with word counts
wordCounts = defaultdict(lambda: 0)
with open(sys.argv[1]) as f:
    for line in f:
        words = re.split(delimRegEx, line)
        for w in words:
            if w != "":
                wordCounts[w] += 1

# Sort by word count in reverse order
sortedWordCounts = sorted(wordCounts.items(), key=lambda item: item[1], reverse=True)

# Print the 10 most frequent words
for word, count in sortedWordCounts[0:10]:
    print("{0:10} {1}".format(count, word))
