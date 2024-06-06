class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        def checkNeighbor(i, j):
            if (i, j) in visited:
                return
            if  0 <= i < rows and 0 <= j < cols :
                if grid[i][j] == "1":
                    visited.add((i, j))
                    checkNeighbor(i + 1, j)
                    checkNeighbor(i, j + 1)
                    checkNeighbor(i - 1, j)
                    checkNeighbor(i, j - 1)
            else:
                return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    numIslands += 1
                    visited.add((i, j))
                    checkNeighbor(i + 1, j)
                    checkNeighbor(i, j + 1)
        return numIslands