class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows//2):
            mat[i], mat[rows-i-1] = mat[rows-i-1], mat[i]
        
        for i in range(rows):
            for j in range(i, cols):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        
