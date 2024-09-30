class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or visited[i][j] or grid[i][j] == 'W':
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 'L':
                    count += 1
                    dfs(i, j)

        return count
