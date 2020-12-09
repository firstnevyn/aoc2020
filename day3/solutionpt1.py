#!/bin/python3

# 8-9 x: xxxxxxxrk
lines=[]
count = 0
def test(line, indexno):
    if line[indexno] == '#':
        return 1
    return 0


count=0
myindex=0
myfile= open("input")
for line in myfile:
    count = count + test(line,myindex)
    myindex = (myindex+3) % len(line.strip())
    print(line.strip())

print (count)
