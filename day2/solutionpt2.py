#!/bin/python3

# 8-9 x: xxxxxxxrk
import re
lines=[]
count = 0
re = re.compile(":-\s")
def test(line):
    if bool(line[3][line[0]-1] == line[2]) ^ bool(line[3][line[1]-1] == line[2])  :
        return 1
    return 0



myfile= open("input")
for line in myfile:
    myline=line.replace(":", " ").replace("-", " ").strip().split()
    minimum = int(myline[0])
    myline[0] = minimum
    maximum = int(myline[1])
    myline[1] = maximum
    count = count + test(myline)


print (count)
