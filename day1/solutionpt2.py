#!/bin/python3

with open("input") as file:
    inputlist = [int(line.strip()) for line in file]

print(inputlist)

listindex = 0
while listindex < len(inputlist):
    remaining = 2020 - inputlist[listindex]
    innerindex = listindex+1
    while innerindex < len(inputlist):
        if (remaining - inputlist[innerindex]) in inputlist:
            print(inputlist[listindex], inputlist[innerindex], remaining - inputlist[innerindex],  inputlist[listindex]*inputlist[innerindex]*(remaining-inputlist[innerindex]))
        innerindex = innerindex + 1
    listindex = listindex + 1


