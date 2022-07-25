"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #11 - Stonks (stonks.py)


Author: Chris Lai

Difficulty Level: 8/10

Background: Paul recently got a nice bonus from work and wanted to invest it into the 
stock market. In order to maximize his profit, Paul analyzed some data from recent 
transactions in order to find out which combination of buying and selling stocks would 
net the highest earnings.

Prompt: Given a list of prices (prices[i]) collected throughout the day, find the highest 
profit that Paul can earn if he buys the stock during any hour of the day and then sells 
it during the same day. In total, Paul may buy/sell a total of two times per day, with 
the condition that he must sell everything before buying again.

Constraints: The number of prices “n” in the list are constrained to 24 >= n > 0 and 
the prices “i” must be constrained to 10^5 >= i >= 0.

Test Cases:
Input: [1, 2, 3, 4, 5, 0], Output: 4
Buy during hour 1 (price = 1), sell during hour 5 (price = 5), net profit = 5 - 1 = 4

Input: [7, 5, 3, 2, 1], Output: 0
DO NOT BUY (declining prices, no profit possible)

Input: [1, 3, 3, 5, 4, 0, 3, 8, 5, 5], Output: 12
Buy during hour 1 (price = 1), sell during hour 4 (price = 5), net profit = 5 - 1 = 4. 
Then, buy during hour 6 (price = 0), sell during hour 8 (price = 8), net profit = 8 - 0 = 8. 
Total profit = 4 + 8 = 12.
"""

from sys import dont_write_bytecode


class Solution:
    def stonks(self, prices):
        # type prices: list
        # return type: int

        # lowest = prices.index(min(prices))

        # highest = prices.index(max(prices))

        # length = len(prices)

        # #checks if the lowest is not at the end of the list 
        # if lowest != (length-2):
            

        
        # #returns that there is no good buys
        # else:
        #     dontbuy = "DO NOT BUY (declining prices, no profit possible)"
        #     return dontbuy
        

        # return length

        
        # Consider the following: Since there are two transactions possible, there will be two
        # "windows" of opportunity for Paul to buy and sell stock. These two windows must be from
        # [0->k], and from [k+1->len(prices)]. The maximum profit will be the the profit from the
        # first window added to the second window. To solve for the maximum profit in this problem
        # statement, we would therefore need to establish the two sliding windows, find the maximum
        # profit from each window, then add them together. 

        # TODO: Analyze first window (forwards profit)
        min_price_1 = 100000 # Set min price to max range for prices: 10^5, adjustible
        profit_1 = []  # Set up profit margin in the first window
        max_profit_1 = 0 # Current max profit is 0

        # Traverse through prices in the forward direction to find profits using x as pointer
        for x in prices: # x represents time (hours in a day)
            if min_price_1 > x:
                # If x is less than the previous min, assign a new minimum to current value x
                min_price_1 = x
            else:
                # Otherwise, if x is not a new minimum, adjust the maximum profit variable
                # The max profit variable ONLY CHANGES when the current profit: x - minimum price
                # is greater than the previous profit.
                max_profit_1 = max(max_profit_1, x - min_price_1)

            # Append the profit found to the first list. At the end of the algorithm, the profit_1 list will
            # contain the maximum profits found through all hours of the day (all items in the prices list) 
            profit_1.append(max_profit_1)

        # TODO: Analyze second window (backwards profit)
        max_price_2 = 0 # Set max price to min range for prices: 0, adjustible
        profit_2 = [0]*len(prices) # Set up profit margin in the second window, moving backwards cannot use append
        max_profit_2 = 0 # Current max profit is 0

        # Traverse through prices in the backwards direction
        for i in range(len(prices) - 1, -1, -1): # Iterate over len(prices) -> 0 inclusive, decrement by 1
            x = prices[i] # Set a seperate variable "x" equal to the contents of prices, counting backwards
            if x > max_price_2: 
                # If the current pointer x is greater than maximum price, set max price equal to current pointer x
                max_price_2 =  x
            else:
                # If the current pointer x is less than maximum price, then there is an opportunity to make profit.
                # Calcaulte the profit at the current location by subtracting x by max_price_2. (x is smaller!)
                # If the profit calculated is greater than the maximum profit, assign the new value to max_profit,
                # Otherwise, the maximum profit stays the same.
                max_profit_2 = max(max_profit_2, max_price_2 - x)

            # (Similar to append but backwards) Insert the maximum profit available at this hour into the profit_2
            # list (second window) and repeat for all items in the list
            profit_2[i] = max_profit_2

        # TODO: Calculate max profit from the two windows
        max_profit = 0 # Default variable
        for i in range(len(prices)): # Iterate across all items in the list
            # Maximum profit at given time is equivalent to the maximum profit calculated from each window summed together
            sum_profit = profit_1[i] + profit_2[i]
            if sum_profit > max_profit: # If the current sum is greater than the maximum profit, assign max profit to the current sum
                max_profit = sum_profit
        
        print(profit_1)
        print(profit_2)

        return max_profit # Return solution



def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.stonks(array)
    print(ans)

if __name__ == "__main__":
    main()