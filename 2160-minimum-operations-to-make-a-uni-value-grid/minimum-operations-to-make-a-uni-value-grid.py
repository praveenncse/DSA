class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        if any(abs(v-u)%x for v,u in pairwise(chain(*grid))): return -1
        return sum(map(abs,map(sub,chain(*grid),repeat(median_low(chain(*grid))))))//x