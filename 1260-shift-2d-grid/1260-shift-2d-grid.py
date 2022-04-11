class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r = len(grid)
        while k>0:
	        ce=grid[-1].pop()
	        for i in range(r-1):
		        grid[i].insert(0,ce)
		        ce=grid[i].pop()
	        grid[-1].insert(0,ce)
	        k-=1  
        return grid