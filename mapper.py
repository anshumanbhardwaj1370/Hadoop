#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
c=1
m=None
n=None
p=None
a=[]
b=[]

for line in sys.stdin:
        # to remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        words = line.split()
        # we are looping over the words array and printing the word
        # with the count of 1 to the STDOUT
 #       print(words)

        if c==1:
                m=int(words[0])
                n=int(words[1])
        elif c==2:
                p=int(words[1])
                print("{} {}".format(m,p))
        else:
                if c<=m+2:
                        a.append(words)
                else:
                        b.append(words)
        c+=1
        # print(c)

for i in range(m):
        for j in range(p):
                ans=0
                for k in range(n):
                        ans+=int(a[i][k])*int(b[k][j])
                print("{} {} {}".format(i,j,ans))
