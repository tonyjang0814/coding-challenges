class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen1,seen2 = dict(),dict()
        for char in s:
            if char in seen1:
                seen1[char] += 1
            else:
                seen1[char] = 1
                
        for char in t:
            if char in seen2:
                seen2[char] += 1
            else:
                seen2[char] = 1
        
        for key in seen1.keys():
            if key not in seen2:
                return False
            elif seen1[key] != seen2[key]:
                return False
        return True