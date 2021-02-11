class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max,curSum = nums[0],nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i],curSum+nums[i])
            _max = max(_max,curSum)
        return _max