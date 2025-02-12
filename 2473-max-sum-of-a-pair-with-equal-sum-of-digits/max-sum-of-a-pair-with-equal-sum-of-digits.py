class Solution:
    def numcal(self, n):
            return sum(int(digit) for digit in str(n))

    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = defaultdict(list)
        for num in nums:
            digit_sum = self.numcal(num)
            digit_sum_map[digit_sum].append(num)

        max_sum = -1
        for group in digit_sum_map.values():
            if len(group) > 1:
                group.sort(reverse=True)
                pair_sum = group[0] + group[1]
                max_sum = max(max_sum, pair_sum)

        return max_sum