class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left = list()
        for i in range(n):
            left.append(1)
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        
        right = 1
        for i in reversed(range(0,n)):
            left[i] = left[i]*right
            right *= nums[i]
        return left