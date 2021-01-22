class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # def countNum(matrix,num):
        #     n = len(matrix)
        #     i=0
        #     count = 0
        #     while i < n:
        #         _break = False
        #         j = 0
        #         while j < n:
        #             if matrix[i][j] <= num:
        #                 count += 1
        #             elif matrix[i][j] > num:
        #                 _break = True
        #             if _break:
        #                 break
        #             j += 1
        #         i += 1
        #     return count
        def countNum(matrix,num):
            n = len(matrix)
            row,col=0,n-1
            count = 0
            while row<n and col >= 0:
                if matrix[row][col] <= num:
                    count += col + 1
                    row += 1
                else:
                    col-=1
            return count
                
        
        n = len(matrix)
        _min = matrix[0][0]
        _max = matrix[n-1][n-1]
        
        left,right = _min,_max
        while left < right:
            mid = (right-left)//2 + left
            count = countNum(matrix,mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return right
        
#                       2         6  8  8
#         1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#                       2          m l,r r