class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        contents = dict()
        for num in nums:
            if num in contents:
                return num
            else:
                contents[num] = 1
        
        