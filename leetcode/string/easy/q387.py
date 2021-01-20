class Solution:
    def firstUniqChar(self, s: str) -> int:
        content = dict()
        for char in s:
            content[char] = content.get(char,0) + 1
        
        character = None
        for char in content:
            if content[char] == 1:
                character = char
                break

        if character is None:
            return -1
        else:
            for idx,char in enumerate(s):
                if char == character:
                    return idx