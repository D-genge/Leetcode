class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        rows, cols = len(grid[0]), len(grid)

        def checkVisited(i, j, areaCount):
            if (i, j) in visited:
                return
            if 0 <= i < rows and 0 <= j < cols:
                if grid[i][j] == 1:
                    maxArea = max(maxArea, areaCount)
                    visited.add((i, j))
                    checkVisited(i+1, j, areaCount+1)
                    checkVisited(i-1, j, areaCount+1)
                    checkVisited(i, j+1, areaCount+1)
                    checkVisited(i, j-1, areaCount+1)
            return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i,j))
                    checkVisited(i+1, j, 1)
                    checkVisited(i, j+1, 1)

        return maxArea