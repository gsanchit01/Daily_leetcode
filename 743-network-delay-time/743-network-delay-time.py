class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited, matrix = [float('inf')] * n, [[float('inf')] * n for _ in range(n)]
        for u, v, w in times:
            matrix[u-1][v-1] = w
        q = [(0, k-1)]
        visited[k-1] = 0
        while q:
            cur_v, cur_n = heapq.heappop(q)
            for nei_n, nei_v in enumerate(matrix[cur_n]):
                if visited[nei_n] > cur_v + nei_v:
                    visited[nei_n] = cur_v + nei_v
                    heapq.heappush(q, (visited[nei_n], nei_n))
        ret = max(visited)
        return ret if ret != float('inf') else -1
