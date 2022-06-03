import os

def create_grid(x: int, y: int):
    grid = []
    gridline = []
    for _ in range(x):
        gridline.append(0)
    for _ in range(y):
        grid.append(list(gridline))
    return grid

def create_line(grid, x1:int, y1:int, x2:int, y2:int):
    if x1 == x2: 
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1
        return
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1
        return
    while x1 != x2 and y1 != y2:
        grid[y1][x1] += 1
        if (x1 < x2):
            x1 += 1
        if (x1 > x2):
            x1 -= 1
        if (y1 < y2):
            y1 += 1
        if (y1 > y2):
            y1 -= 1
    grid[y1][x1] += 1

def count_grid_overlaps(grid, x_points:int, y_points:int):
    result = 0
    for x in range(0, x_points):
        for y in range(0, y_points):
            if (grid[y][x] > 1):
                result += 1
    return result


input = open(os.getcwd() + "\Day_05\input.txt").read().splitlines()
grid = create_grid(1000,1000)
for i in input:
    points = i.split(" -> ")
    start_point = points[0].split(',')
    end_point = points[1].split(',')
    create_line(grid, int(start_point[0]), int(start_point[1]), int(end_point[0]), int(end_point[1]))

print(count_grid_overlaps(grid, 1000, 1000))