class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = 0
        odd_sum = 0
        mod = 10**9 + 7
        for val in arr:
            prefix_sum += val
            odd_sum += prefix_sum % 2
        odd_sum += (len(arr) - odd_sum ) * odd_sum
        return odd_sum % mod