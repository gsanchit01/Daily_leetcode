class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        len_row = len(matrix[0])
        len_col = len(matrix)
        new_matrix = [[0 for i in range(len_col)] for j in range(len_row)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[j][i] = matrix[i][j]
        
        return new_matrix