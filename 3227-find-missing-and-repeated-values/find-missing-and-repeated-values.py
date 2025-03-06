class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        attendance = [False] * (n * n + 1)
        duplicate = -1

        for i in range(n):
            for j in range(n):
                if attendance[grid[i][j]]:
                    duplicate = grid[i][j]
                else:
                    attendance[grid[i][j]] = True

        for i in range(1, n * n + 1):
            if not attendance[i]:
                return [duplicate, i]
        return []