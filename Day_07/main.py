from math import dist
import os
import statistics

def calculate_needed_fuel_median(positions: list) -> int:
    return sum(map(lambda x: abs(x - statistics.median(positions)), positions))

def calculate_needed_fuel_mean(positions: list) -> int:
    min_fuel_cost = 1e9
    for index in range(min(positions), max(positions)):
        fuel_cost = 0
        for position in positions:
            distance = abs(position - index)
            fuel_cost += distance + ((distance * (distance - 1)) // 2)
        if fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
    return min_fuel_cost

input = list(map(int, open(os.getcwd() + "\Day_07\input.txt").read().split(',')))

print(calculate_needed_fuel_median(input))
print(calculate_needed_fuel_mean(input))