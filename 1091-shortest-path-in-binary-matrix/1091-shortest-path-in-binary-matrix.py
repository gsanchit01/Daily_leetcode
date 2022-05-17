class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        mx_rows, mx_cols = len(grid)-1, 0
        if mx_rows > 0: mx_cols = len(grid[0])-1
            
        # check if start and end are open??
        if grid[0][0] != 0 or grid[mx_rows][mx_cols] != 0 : return -1
        
        d = [-1, 0, 1]
        moves = [(x,y) for x in d for y in d ]
        moves.remove((0,0)) # 0,0 moves doesn't lead anywhere
        # print(moves)
        
        def next_neighbor(i, j):
            for mi, mj in moves:
                ni, nj = i+mi, j+mj
                if ni < 0 or mx_rows < ni : continue # boundary check
                if nj < 0 or mx_cols < nj : continue # boundary check
                
                if grid[ni][nj] != 0 : continue # open cell

                # print(f"{i}+{mi}={ni}, {j}+{mj}={nj}")
                yield (ni, nj)                
        
        q = deque()
        q.append((0,0)) # start cell
        grid[0][0] = 1 # set initial distance
        
        # till there are cells in queue
        while q:
            ci, cj = q.popleft()
            distance = grid[ci][cj]
            # if we reached the exit, return
            if (ci, cj) == (mx_rows, mx_cols): return distance
            
            for ni, nj in next_neighbor(ci, cj):
                # print(ni, nj)
                grid[ni][nj] = distance + 1
                q.append((ni,nj))
        
        return -1