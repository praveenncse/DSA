class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans=0
        r=len(matrix)
        c=len(matrix[0])
        maxx=0
        for dig in range(c):
            ans += matrix[0][dig]
        for dig in range(1,r):
            ans += matrix[dig][0]
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == 1 and matrix[i][j-1] > 0 and matrix[i-1][j] > 0 and matrix[i-1][j-1] > 0:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                ans += matrix[i][j]
        return ans