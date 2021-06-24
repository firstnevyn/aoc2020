#!/bin/python3

myfile= open("input")
entries=[]
entry={}
for line in myfile:
    if line.strip():
        for element in line.strip().split(" "):
            stuff = element.split(":")
            entry.update({stuff[0]: stuff[1]})
    else:
        entries.append(entry)
        entry = {}

entries.append(entry)
count=0
requiredset={"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} #, "cid"}
for passport in entries:
    print (set(passport.keys()), set(passport.keys()).issuperset(requiredset))
    if set(passport.keys()).issuperset(requiredset):
         count = count + 1
print(count, len(entries))

