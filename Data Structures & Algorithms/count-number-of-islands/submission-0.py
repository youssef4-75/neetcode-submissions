class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        passed = set()
        res = 0
        for i, line in enumerate(grid):
            for j, land in enumerate(line):
                if land == "0":
                    continue
                if land == "1" and (i, j) in passed:
                    continue
                res += 1
                self.eat(grid, i, j, passed)
        return res

    def eat(self, grid, start_i, start_j, passed):
        if start_i < 0 or start_i >= len(grid) or start_j < 0 or start_j >= len(grid[0]):
            return
        if grid[start_i][start_j] == "0" or (start_i, start_j) in passed:
            return
        
        passed.add((start_i, start_j))

        self.eat(grid, start_i+1, start_j, passed)
        self.eat(grid, start_i-1, start_j, passed)
        self.eat(grid, start_i, start_j+1, passed)
        self.eat(grid, start_i, start_j-1, passed)

        

                
