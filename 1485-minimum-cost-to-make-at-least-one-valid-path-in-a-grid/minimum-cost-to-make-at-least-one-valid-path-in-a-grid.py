class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cost = [[float('inf')] * n for _ in range(m)]
        heap = [(0, 0, 0)] 
        cost[0][0] = 0
        while heap:
            cur_cost, x, y = heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return cur_cost
            for i, (dx, dy) in enumerate(directions, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cur_cost + (grid[x][y] != i)
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heappush(heap, (new_cost, nx, ny))