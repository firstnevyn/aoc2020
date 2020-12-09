#!/bin/python3

# 8-9 x: xxxxxxxrk
import re
re = re.compile(":-\s")
myfile= open("input")
for line in myfile:
    minimum=line.replace(":", " ").replace("-", " ").strip().split()
    minimum[0] = int(minimum[0]
    minimum[1] = int(minimum[1]
print(minimum)



