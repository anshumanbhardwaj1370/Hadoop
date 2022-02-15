#!/usr/bin/env python

from operator import itemgetter
import sys

c=[]
cnt=0

# read the entire line from STDIN
for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # splitting the data on the basis of tab we have provided in mapper.py


        if cnt==0:
                #print(line.split())
                lis= line.split()
                c=[[0]*int(lis[1])]*int(lis[0])
        else:
                i,j,value = line.split()
                i=int(i)
                j=int(j)
                c[i][j]=int(value)

        cnt+=1

for x in c:
    for y in x:
        print(y,end=" ")
    print()