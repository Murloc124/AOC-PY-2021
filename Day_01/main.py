import os
from re import sub

submarineReport = open(os.getcwd() + "\Day_01\input.txt").read().split()
measurementIncreases = 0
#Part 1
for l in range(len(submarineReport) - 1):
    if (int(submarineReport[l]) < int(submarineReport[l+1])):
        measurementIncreases += 1
print(measurementIncreases)
measurementIncreases = 0
#Part 2
for l in range(len(submarineReport)-3):
    A = int(submarineReport[l]) + int(submarineReport[l+1]) + int(submarineReport[l+2])
    B = int(submarineReport[l+1]) + int(submarineReport[l+2]) + int(submarineReport[l+3])
    if (A < B):
        measurementIncreases += 1
print(measurementIncreases)