class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        majority,count = 0,0
        for num in nums:
            if count == 0:
                majority = num
                count = 1
            else:
                if num == majority:
                    count += 1
                else:
                    count -= 1
        return majority