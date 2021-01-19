class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1:
        #     return 1

        left,right = 0,0
        content = dict()
        for char in s:
            content[char] = 0
        
        _max = 0
        left,right = 0 ,0
        while right < len(s):
            content[s[right]] += 1
            if content[s[right]] > 1:
                content[s[right]] -= 1
                content[s[left]] -= 1
                left += 1
                right -= 1
            else:
                _max = max(_max,right-left+1)
            right += 1
        return _max