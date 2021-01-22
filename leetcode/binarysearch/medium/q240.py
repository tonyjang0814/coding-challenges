class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binarySearch(_list,num):
            left,right = 0,len(_list)-1
            while left <= right:
                mid = (right-left)//2 + left
                if _list[mid] == num:
                    return True
                elif _list[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        for _list in matrix:
            if target >= _list[0] and target <= _list[-1]: # if target is in row, do binary search
                if binarySearch(_list,target):
                    return True
        return False