class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findIndices(nums,mid):
            left,right = mid,mid
            while nums[left] == nums[mid] and nums[right] == nums[mid]:
                left -= 1
                right += 1
                if left < 0 or right >= len(nums):
                    break
            
            while left >= 0 and nums[left] == nums[mid]:
                left -= 1
            while right < len(nums) and nums[right] == nums[mid]:
                right += 1
            return [left+1,right-1]
        
        if not nums:
            return [-1,-1]
        left,right = 0,len(nums) - 1
        
        while left<=right:
            mid = (right-left)//2 + left
            if nums[mid] == target:
                return findIndices(nums,mid)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1,-1]