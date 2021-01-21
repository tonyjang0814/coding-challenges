class Solution:
    def mySqrt(self, x: int) -> int:
        
        l , r = 1 , x
        while l <= r :
	        mid = (l+r)//2
	        pivot = mid ** 2 
	        if pivot == x :
		        return mid 
	        elif pivot <=x :
		        l = mid +1 
	        else :
		        r = mid -1 
        return l-1