class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(mat)
        cols = len(mat[0])
        is_first_row = False
        is_first_col=False

        for i in range(rows):
            if mat[0][i] ==0:
                is_first_row = True
                break
        for i in range(cols):
            if mat[i][0] ==0:
                is_first_col = True
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if mat[i][j]==0:
                    mat[i][0]=0
                    mat[0][j]=0

        for i in range(1, rows):
            for j in range(1, cols): 
                if mat[i][0] ==0 or mat[0][j]==0:
                    mat[i][j]=0

        if is_first_row:
            for i in range(cols):
                mat[0][i]=0
        if is_first_col:
            for j in range(rows):
                mat[j][0]=0


        
        

        
