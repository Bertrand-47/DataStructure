class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix [i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i]= temp
            
        length = len(matrix)
        
        for i in range(len(matrix)):
            for j in range(int(len(matrix)/2)):
                temp = matrix[i][j]
                matrix[i][j]= matrix[i][length-1-j]
                matrix[i][length-1-j] = temp
            