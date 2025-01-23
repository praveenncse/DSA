class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        leftsum=0
        rightsum=s

        for i in range(0,len(nums)):
            leftsum=leftsum+nums[i]
            if leftsum==rightsum:
                return i
            rightsum=rightsum-nums[i]
        return -1