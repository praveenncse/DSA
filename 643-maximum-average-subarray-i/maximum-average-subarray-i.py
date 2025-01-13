class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currsum = sum(nums[:k])
        maxsum = currsum

        for i in range(k, len(nums)):
            currsum += nums[i] - nums[i - k]
            maxsum = max(maxsum, currsum)

        
        return maxsum / k