#!/bin/python3

# 8-9 x: xxxxxxxrk
lines=[]
count = 0
def test(line):
    occurance = line[3].count(line[2])
    if occurance >= line[0] and occurance <= line[1]:
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
