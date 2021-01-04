class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         # method 1: Using state transition method.
#         n = len(prices)
#         if n <= 1: # can not make profit at all
#             return 0
        
#         in_hand,no_stock,sold = list(),list(),list()
#         # initilaise three arrays.
#         for i in range(n):
#             in_hand.append(0)
#             no_stock.append(0)
#             sold.append(0)
            
#         in_hand[0] -= prices[0] # buying stock at first stage costs money.
        
#         for i in range(1,n):
#             no_stock[i] = max(no_stock[i-1],sold[i-1])
#             in_hand[i] = max(in_hand[i-1],no_stock[i-1]-prices[i])
#             sold[i] = in_hand[i-1] + prices[i]
        
#         return max(no_stock[-1],in_hand[-1],sold[-1])
        
        # method 2: Using recursion and memoization.
        n = len(prices)
        if n <= 1: # can not make profit at all
            return 0
        self.memo = dict()
        max_profit = self.findMax(prices,0,n)
        return max_profit
    
    def findMax(self,prices,curr,n):
        if curr >= n: # if index gone out of bound.
            return 0
        elif curr in self.memo: # if max value of particular index is calcualted already, just return its value
            return self.memo[curr]
        
        #   for each index, there is two option.
        #   1. making profit by buying stock and selling at appropriate timing.
        max_profit = 0
        for i in range(curr+1,n):
            if prices[curr] < prices[i]: # if we can make profit,
                #       There are two options to make profit when buying a stock ar curr index.
                #   -   sell at ith index and find the max profit after cool down period.
                #   -   do not sell and see if we can make more money by skip selling at ith index. 
                max_profit = max(max_profit, prices[i]-prices[curr] + self.findMax(prices,i+2,n))
     
        #   2. just skip buying at current index and find the max profit for the next index.
        max_profit = max(max_profit,self.findMax(prices,curr+1,n))
        self.memo[curr] = max_profit
        return max_profit
        
            