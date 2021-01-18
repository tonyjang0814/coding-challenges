roman_number = {
	'I' : 1,
	"V" : 5,
	"X" : 10,
	"L" : 50,
	"C" : 100,
	"D" : 500,
	"M" : 1000	
}

class Solution:
    def romanToInt(self, s: str) -> int:
        _sum = 0
        s = list(s)
        prev = None
        for i in range(len(s)):
            if i < len(s) - 1:
                if roman_number[s[i]] < roman_number[s[i+1]]:
                    _sum -= roman_number[s[i]]
                else:
                    _sum += roman_number[s[i]]
        _sum += roman_number[s[i]]
        return _sum