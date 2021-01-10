class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #   method 1
        # result = 0
        # #   using the exclusive XOR,
        # #   a ^ 0 = a
        # #   a ^ a = 0
        # for num in nums:
        #     result ^= num
        # return result
        
        
        #   method 2 - dictionary
        seen = dict()
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        for key in seen.keys():
            if seen[key] == 1:
                return key