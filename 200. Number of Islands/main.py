class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        if not grid:
            return 0

        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"  

                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)
        return island_count
