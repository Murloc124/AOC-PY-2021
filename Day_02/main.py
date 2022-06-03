import os

class Submarine:
    def __init__(self) -> None:
        self.pos_h=0
        self.pos_v=0
        self.aim=0
    def forward(self, units) -> None:
        self.pos_h += units
        self.pos_v+=self.aim*units
    def down(self, units) -> None:
        self.aim += units
    def up(self, units) -> None:
        self.aim -= units
    def finalize(self) -> int:
        return self.pos_h * self.pos_v

input = open(os.getcwd() + "\Day_02\input.txt").read().splitlines()
solution = Submarine()
for move in input:
    command = move.split()[0]
    if (command == "forward"):
        solution.forward(int(move.split()[1]))
    if (command == "down"):
        solution.down(int(move.split()[1]))
    if(command=="up"):
        solution.up(int(move.split()[1]))
print(solution.finalize())