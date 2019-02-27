grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]



# calculate how many island
count = 0

for c, row in enumerate(grid):
    for r, item in enumerate(row):
        count += 1
        if grid[c+1][r] == 1 or grid[c][r+1] == 1:
            count -= 1

print(count)



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for c, row in enumerate(grid):
            for r, item in enumerate(row):
                count += 1
                if grid[c + 1][r] == 1 or grid[c][r + 1] == 1:
                    count -= 1
                    return count


# Perimeter!!!!
count = 0

for c, row in enumerate(grid):
    for r, item in enumerate(row):
        if item == 1:
            count += 4
            if c+1 < len(grid) and grid[c+1][r] == 1:
                count -= 2
            if r+1 < len(row) and grid[c][r+1] == 1:
                count -= 2

print(count)



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for c, row in enumerate(grid):
            for r, item in enumerate(row):
                if item == 1:
                    count += 4
                    if c + 1 < len(grid) and grid[c + 1][r] == 1:
                        count -= 2
                    if r + 1 < len(row) and grid[c][r + 1] == 1:
                        count -= 2
        return count