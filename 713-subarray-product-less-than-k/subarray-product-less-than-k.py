class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res=0
        prod=1
        l=0

        for r in range(len(nums)):
            prod*=nums[r]
            while prod>=k and l<=r:
                prod=prod//nums[l]
                l+=1
            res+=r-l+1
            
        return res