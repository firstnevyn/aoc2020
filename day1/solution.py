#!/bin/python3

with open("input") as file:
    inputlist = [int(line.strip()) for line in file]

print(inputlist)
lookupset=set(inputlist)
listindex = 0
while listindex < len(inputlist):
    testednumber = inputlist[listindex]
    if (2020-testednumber) in lookupset:
        print( testednumber * (2020 - testednumber))
    listindex = listindex + 1


