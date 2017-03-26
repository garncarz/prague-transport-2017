#!/usr/bin/python

import random, sys

if len(sys.argv) < 3:
    print "Usage details: big_input_generator.py <city_cnt> <edge_cnt>"
    sys.exit(666)

outfile = open('big_in.txt', 'w')
city_cnt = int(sys.argv[1])
edge_cnt = int(sys.argv[2])

outfile.write(str(city_cnt) + '\n')
for count in range(edge_cnt):
    #Get a random number.
    fr = random.randint(0, city_cnt)
    to = random.randint(0, city_cnt)
    weight = random.randint(1, sys.maxsize)
    outfile.write(str(fr) + ' ' + str(to) + ' ' + str(weight) + '\n')

outfile.close()
