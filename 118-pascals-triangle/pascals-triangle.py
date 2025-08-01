class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        triangle.append([1])
        for i in range(numRows-1):
            temp=[1]
            for j in range(0,i):
                temp.append(triangle[i][j]+triangle[i][j+1])
            temp.append(1)
            triangle.append(temp)
        return triangle