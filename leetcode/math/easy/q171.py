class Solution:
    def titleToNumber(self, s: str) -> int:
        s = list(s)
        factor = 1
        _sum = 0
        for i in reversed(s):
            _sum += (ord(i)-ord('A')+1)*factor
            factor *= 26
        return _sum