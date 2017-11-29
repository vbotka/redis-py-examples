#!/usr/bin/python3
# Tested with python 3.6.3, python-redis 2.10.5 and redis 4.0.1

import redis

LOG_FILES = ['/var/log/dpkg.log', ]
LOG_SEPARATOR = ' '
CSV_SEPARATOR = ';'

def read_log(log_file):
    ''' This function reads log_file and put the status into the database '''
    f = open(log_file, 'r')
    for line in f:
        l = line.split(LOG_SEPARATOR)
        word = l[0] + ' ' + l[1][:-3]
        r.zincrby(l[2], word, 1)
    f.close()

def write_csv(status):
    ''' This function reads the database and writes the status CSV file '''
    f = open(status.decode() + '.csv', 'w')
    l = r.zrange(status, 0, -1, 'DESC', 'WITHSCORES')
    for x in l:
        f.write(x[0].decode() + CSV_SEPARATOR + str(int(x[1])) + '\n') 
    f.close()

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushdb()

for log_file in LOG_FILES:
    read_log(log_file)

for status in r.keys():
    write_csv(status)
