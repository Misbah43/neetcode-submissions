class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit=0
        # left=0
        # right=len(prices)-1
        # if right==-1:
        #     max_profit=0
        # else:
        #     while left<right:
        #         profit=prices[right]-prices[left]
        #         max_profit=max(max_profit,profit)
        #         if max_profit
        #         left+=1
        #         right-=1
        # return max_profit
        # max_profit=0
        # for i ,price in enumerate(prices):
        #   j=i+1
        #   for j ,price in enumerate(prices):
        #      if j==-1:
        #         max_profit=0
        #      else:
        #       profit=prices[j]-prices[i]
        #       max_profit=max(max_profit,profit)
        #       j+=1
        #   i+=1
        # return max_profit
         max_profit=0
         lowest_price=prices[0]
         for price in prices:
            if price<lowest_price:
                lowest_price=price
            else:
                profit=price-lowest_price
                max_profit=max(profit,max_profit)
         return max_profit

     


        