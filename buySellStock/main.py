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