class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        passed = set()
        max_area = area = 0
        for i, line in enumerate(grid):
            for j, land in enumerate(line):
                if land == "0":
                    continue
                if land == "1" and (i, j) in passed:
                    continue
                area = self.eat(grid, i, j, passed)
                if area > max_area:
                    max_area = area
        return max_area

    def eat(self, grid, start_i, start_j, passed):
        if start_i < 0 or start_i >= len(grid) or start_j < 0 or start_j >= len(grid[0]):
            return 0
        if grid[start_i][start_j] == 0 or (start_i, start_j) in passed:
            return 0
        start = 1
        passed.add((start_i, start_j))

        start += self.eat(grid, start_i+1, start_j, passed)
        start += self.eat(grid, start_i-1, start_j, passed)
        start += self.eat(grid, start_i, start_j+1, passed)
        start += self.eat(grid, start_i, start_j-1, passed)

        
        return start

        

                
