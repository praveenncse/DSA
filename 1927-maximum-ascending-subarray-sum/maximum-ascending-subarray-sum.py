class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currsum=maxsum=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                currsum+=nums[i]
            else:
                currsum=nums[i]
            maxsum=max(currsum,maxsum)
        return maxsum