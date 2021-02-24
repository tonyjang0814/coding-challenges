class Solution:
    # solution 1 : Recursive way O(2^n)
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums: #if empty list is given
#             return 0
#         elif len(nums) == 1:
#             return 1
        
#         self.max_len = 0
#         self.findMaxLIS(nums,0,float('-inf'),0)
        
#         return self.max_len
    
#     def findMaxLIS(self,nums,index,prev_num,seq_len):
#         if index >= len(nums):
#             self.max_len = max(self.max_len,seq_len)
#             return
        
#         if nums[index] > prev_num:
#             self.findMaxLIS(nums,index+1,nums[index],seq_len+1)
#         self.findMaxLIS(nums,index+1,prev_num,seq_len)
        
        
    #   Solution 2: Dynammic Programming O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        dp = [1]*(n + 1)
        
        for i in range(n):
            for j in range(i):
                if (nums[j] < nums[i]) and (dp[i] <= dp[j]):
                    dp[i] = dp[j] + 1
        return max(dp)
        
        