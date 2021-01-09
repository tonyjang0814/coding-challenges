class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        #   finding possible water level from left and right traversal.
        #   get the minimum of those value and subtract by height[i] to get actual water storage value on that index.
        #   sum of such array is the total water amount of water stored in map.
        left_water,right_water = list(),list()
        for i in range(n):
            left_water.append(0)
            right_water.append(0)
        
        left_max,right_max = float('-inf'),float('-inf')
        for i in range(n):
            if height[i] > left_max:
                left_max = height[i]
            left_water[i] = left_max
        
        for i in reversed(range(n)):
            if height[i] > right_max:
                right_max = height[i]
            right_water[i] = right_max
        
        for i in range(n):
            left_water[i] = min(left_water[i],right_water[i]) - height[i]
        return sum(left_water)