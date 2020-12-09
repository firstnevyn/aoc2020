#!/bin/python3

# 8-9 x: xxxxxxxrk
lines=[]
count = 0
def test(line, indexno):
    if line[indexno] == '#':
        return 1
    return 0


myfile= open("input")
for line in myfile:
    lines.append(line.strip())

def testarray(across, down):
    count=0
    j=0
    i=0
    while i < len(lines):
       if lines[i][j] == '#': count = count + 1
       j = (j + across) % len(lines[i])
       i = i + down
    return count


print(testarray(1,1) * testarray(3,1) * testarray(5,1) * testarray(7,1) * testarray(1,2))

