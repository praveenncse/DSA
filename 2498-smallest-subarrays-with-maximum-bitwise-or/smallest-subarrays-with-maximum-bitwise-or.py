class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        f = [-1] * 32  

        for i in range(len(nums) - 1, -1, -1):
            t = 1 
            for j in range(32):
                if (nums[i] >> j) & 1:
                    f[j] = i 
                elif f[j] != -1:
                    t = max(t, f[j] - i + 1)
            res[i] = t  
        return res