class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        trans_matrix = [[0] * row for i in range(col)] 
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                trans_matrix[col][row] = matrix[row][col]

        return trans_matrix
