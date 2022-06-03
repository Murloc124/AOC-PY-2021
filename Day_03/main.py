from math import gamma
import os
from tokenize import String

def CalculateGammaRate(input: list) -> str:
    result = ""
    for i in range(len(input[0])):
        count1=0
        count0=0
        for k in range(len(input)):
            if (int(input[k][i]) == 1):
                count1 += 1
            if (int(input[k][i]) == 0):
                count0 += 1
        if (count1>count0):
            result += "1"
        else:
            result += "0"
    return result

def CalculateYpsilonRate(input: list) -> str:
    result = ""
    for i in range(len(input[0])):
        count1=0
        count0=0
        for k in range(len(input)):
            if (int(input[k][i]) == 1):
                count1 += 1
            if (int(input[k][i]) == 0):
                count0 += 1
        if (count1<count0):
            result += "1"
        else:
            result += "0"
    return result

def GetPowerConsumption(GammaRate, YpsilonRate) -> int:
    return int(GammaRate, 2) * int(YpsilonRate, 2)

input = open(os.getcwd() + "\Day_03\input.txt").read().splitlines()
print(GetPowerConsumption(CalculateGammaRate(input),CalculateYpsilonRate(input)))

def Oxygen(input: list, index: int) -> int:
    if (len(input) == 1):
        return int(input[0],2)
    input1 = []
    input0 = []
    for k in range(len(input)):
        if (int(input[k][index]) == 1):
            input1.append(input[k])
        if (int(input[k][index]) == 0):
            input0.append(input[k])
    if (len(input1)>len(input0)):
        return Oxygen(input1, index+1)
    if (len(input1)<len(input0)):
        return Oxygen(input0, index+1)
    else:
        return Oxygen(input1, index+1)

def CO2(input: list, index: int) -> int:
    if (len(input) == 1):
        return int(input[0],2)
    input1 = []
    input0 = []
    for k in range(len(input)):
        if (int(input[k][index]) == 1):
            input1.append(input[k])
        if (int(input[k][index]) == 0):
            input0.append(input[k])
    if (len(input1)>len(input0)):
        return CO2(input0, index+1)
    if (len(input1)<len(input0)):
        return CO2(input1, index+1)
    else:
        return CO2(input0, index+1)

print(CO2(input, 0)*Oxygen(input,0))