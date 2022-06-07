from asyncio.base_futures import _FINISHED
from collections import defaultdict
import os

def next_day(fishes) -> dict[int, int]:
    new_fish_lib = defaultdict(int)
    for timer, n_fish in fishes.items():
        if timer == 0:
            timer = 7
            new_fish_lib[8] += n_fish
        new_fish_lib[timer - 1] += n_fish
    return new_fish_lib

input = list(map(int, open(os.getcwd() + "\Day_06\input.txt").read().split(',')))
fish_lib = {timer: input.count(timer) for timer in set(input)}
print (fish_lib)

for _ in range(256):
    fish_lib = next_day(fish_lib)

print(sum(fish_lib.values()))