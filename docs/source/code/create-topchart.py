#!/usr/bin/python3
# Tested with python 3.6.3, python-redis 2.10.5 and redis 4.0.1

import redis
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
# nltk.download()

file = 'redis.txt'

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushdb()

f = open(file, 'r')
text = f.read()
f.close()
words = word_tokenize(text)

for word in words:
    if wordnet.synsets(word):
        r.zincrby('topchart', word, 1)

ranking = r.zrange('topchart', 0, 10, 'DESC', 'WITHSCORES')
for x in ranking:
    print ("%d\t%s" % (x[1], x[0].decode()))
