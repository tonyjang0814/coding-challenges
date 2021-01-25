class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #   Find pivot index
        #   Based on the number on pivot index, go for another
        #   binary search either to the right or left.

        def binarySearch(nums,left,right,target):
            while left<=right:
                mid = (right-left)//2 + left
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        left,right = 0,len(nums)-1
        pivot = 0
        while left <= right:
            mid = (right-left)//2 + left
            if mid == 0 or mid == len(nums)-1:
                pivot = 0
                break
            elif nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                pivot = mid
                break
            elif nums[mid] < nums[mid+1]:
                left = mid+1

        #   Perform another binary search based on pivot index number.
        if nums[pivot] == target:
            return pivot
        elif pivot == 0:
            for idx,val in enumerate(nums):
                if val == target:
                    return idx
            return -1
        elif nums[0]<=target< nums[pivot]:
            left,right = 0, pivot-1
            return binarySearch(nums,left,right,target)
        else:
            left,right = pivot + 1,len(nums)-1
            return binarySearch(nums,left,right,target)