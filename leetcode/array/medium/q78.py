class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return nums
        elif n == 1:
            ans = list()
            ans.append(nums)
            ans.append([])
            return ans
        
        
        self.ans = list()
        temp = list()
        self.getSubSets(nums,0,n,temp)
        return self.ans
    
    def getSubSets(self,nums,idx,n,temp):
        if idx >= n:
            self.ans.append(temp.copy())
            return
        temp.append(nums[idx])
        self.getSubSets(nums,idx+1,n,temp)
        temp.pop()
        self.getSubSets(nums,idx+1,n,temp)