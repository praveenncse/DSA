class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        A=students
        B=sandwiches
        count = collections.Counter(A)
        n, k = len(A), 0
        while k < n and count[B[k]]:
            count[B[k]] -= 1
            k += 1
        return n - k