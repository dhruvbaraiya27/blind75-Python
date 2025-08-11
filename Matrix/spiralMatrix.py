class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        total = rows*cols
        first_row=0
        last_row = rows - 1
        first_col =0
        last_col = cols - 1
        cnt=0
        result = []
        while cnt< total:
            for i in range(first_col, last_col + 1):
                if cnt < total:
                    result.append(mat[first_row][i])
                    cnt+=1
            first_row +=1
            for i in range(first_row, last_row + 1):
                if cnt < total:
                    result.append(mat[i][last_col])
                    cnt+=1
            last_col -=1
            for i in range(last_col, first_col -1, -1):
                if cnt < total:
                    result.append(mat[last_row][i])
                    cnt+=1
            last_row -=1
            for i in range(last_row, first_row-1, -1):
                if cnt<total:
                    result.append(mat[i][first_col])
                    cnt+=1
            first_col +=1
        return result


        
