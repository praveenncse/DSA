class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        solution = [[] for i in range(numRows)]
        direction = True
        row = -1
        for i in s:
            if direction:
                row += 1
                solution[row].append(i)
                if row == numRows - 1:
                    direction = not direction
            else:
                row -= 1
                solution[row].append(i)
                if row == 0:
                    direction = not direction
        s = ""
        for i in solution:
            s += "".join(i)
        return s