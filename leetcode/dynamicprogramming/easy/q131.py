class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.real_ans = list()          
        potential_ans = list()
        self.partiotionString(s,0,potential_ans)
        # print(self.real_ans)
        return self.real_ans
        
        
    def isPalindrome(self,s,start_idx,end_idx):
        while start_idx < end_idx:
            if s[start_idx] != s[end_idx]:
                return False
            start_idx += 1
            end_idx -= 1
        return True

    def partiotionString(self,s,ibuilder,potential_ans):
        if ibuilder >= len(s):
            self.real_ans.append(potential_ans)
        else:
            for i in range(ibuilder,len(s)):
                if self.isPalindrome(s,ibuilder,i):
                    self.partiotionString(s,i+1,potential_ans+[s[ibuilder:i+1]])