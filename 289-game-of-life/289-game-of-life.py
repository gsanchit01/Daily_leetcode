class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowl = len(board)
        coll = len(board[0])

        def find_live_cell_count(row, col):
            
            rows = [row-1, row, row+1]
            cols = [col-1, col, col+1]
            
            total = -board[row][col]
            for r in rows:
                for c in cols:
                    if 0 <= r < len(board) and 0 <= c < len(board[0]):
                        if board[r][c] in [1, 2]:
                            total += 1
            return total

        for r in range(rowl):
            for c in range(coll):
                cell = board[r][c]
                count = find_live_cell_count(r, c)
                
                if not cell:
                    if count == 3:
                        board[r][c] = 3
                else:
                    if count in [2, 3]:
                        board[r][c] = 2
                    
        for r in range(rowl):
            for c in range(coll):
                if board[r][c] in [2,3]:
                    board[r][c] = 1
                else:
                    board[r][c] = 0           