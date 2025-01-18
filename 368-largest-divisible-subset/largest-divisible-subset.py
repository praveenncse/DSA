class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        # Step 2: Initialize dp and parent arrays
        n = len(nums)
        dp = [1] * n  # dp[i] is the size of the largest subset ending at nums[i]
        parent = [-1] * n  # parent[i] points to the previous index in the subset

        # Step 3: Build the dp array
        max_size = 0
        max_index = -1

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            # Update the largest subset information
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # Step 4: Reconstruct the subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]

        return result[::-1]