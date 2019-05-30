prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
brought = False
profit = 0

for index in range(len(prices)):
    if (index <len(prices)-1) and (prices[index]<prices[index+1]) and (brought == False):
        brought = True
        inPrice = prices[index]
    elif (index < len(prices)-1) and (prices[index] > prices[index+1]) and (brought == True):
        brought = False
        profit += prices[index] - inPrice
    elif (index == len(prices)-1) and (brought == True):
        brought = False
        profit += prices[index] - inPrice

print(profit)


def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        for p in prices:
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p - minPrice)
        return maxProfit



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        brought = False
        profit = 0
        for index in range(len(prices)):
            if (index < len(prices) - 1) and (prices[index] < prices[index + 1]) and (brought == False):
                brought = True
                inPrice = prices[index]
            elif (index < len(prices) - 1) and (prices[index] > prices[index + 1]) and (brought == True):
                brought = False
                profit += prices[index] - inPrice
            elif (index == len(prices) - 1) and (brought == True):
                brought = False
                profit += prices[index] - inPrice
        return profit