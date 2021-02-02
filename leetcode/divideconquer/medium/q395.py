class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or len(s) < k:
            return 0
        elif k == 1:
            return len(s)
        content = Counter(s)
        doDivide = False
        for idx,val in enumerate(s):
            if content[val] < k:
                doDivide = True
                l1 = self.longestSubstring(s[:idx],k)
                l2 = self.longestSubstring(s[idx+1:],k)
                break
        if doDivide:
            return max(l1,l2)
        else:
            return len(s)