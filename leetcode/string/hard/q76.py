class Solution:
    def minWindow(self, s: str, t: str) -> str:
        content = dict()
        for char in t:
            if char in content:
                content[char] += 1
            else:
                content[char] = 1
        
        _len = float('inf')
        ans = ""
        t = list(t)
        left,right =0,0
        temp_cpy = dict()
        # ans = list()
        while right < len(s):
            # print(left)
            # print(right)
            # print("\n")
            if s[right] in content:
                temp_cpy[s[right]] = temp_cpy.get(s[right],0)+1
            
            #   checking if valid substring
            isValid = True

            for char in t:
                if char not in temp_cpy or temp_cpy[char] < content[char]:
                    isValid=False
                    break
            if isValid:
                # if found the valid substring, try tighinging string by moving left pointer.
                # as soon as it breaks the rule, try to find new string by moving right pointer.
                while isValid:
                    if right-left+1 < _len:
                        _len = right-left+1
                        ans = s[left:right+1]
                    # ans.append(s[left:right+1])
                    if s[left] in temp_cpy:
                        temp_cpy[s[left]] -= 1
                        if temp_cpy[s[left]] < content[s[left]]:
                            left += 1
                            break
                        else:
                            left += 1
                    else:
                        left += 1
                right += 1
            else:
                right += 1   
        return ans