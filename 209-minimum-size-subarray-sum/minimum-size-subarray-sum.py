class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=0
        l=0
        length= float('inf')

        for r in range(len(nums)):
            res+=nums[r]
            while res>=target:
                length=min(length,r-l+1)
                res-=nums[l]
                l+=1
        if length==float('inf'):
            return 0
        else:
            return length
  