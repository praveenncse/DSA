class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        s = sorted((nums[i], i) for i in range(n))
        i = 0

        while i < n:
            j = i+1
            while j < n and abs(s[j][0] - s[j-1][0]) <= limit:
                j += 1
            if j > i+1:
                for x, y in enumerate(sorted(s[k][1] for k in range(i, j))):
                    nums[y] = s[i+x][0]
            i = j

        return nums