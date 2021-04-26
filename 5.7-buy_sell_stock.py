def brute_buy_and_sell_stock_once(p):
    """
    Write a program that takes an array denoting the daily stock price, and returns the maximum profit
    that could be made by buying and then selling one share of that stock. There is no need to buy if
    no profit is possible.

    LEETCODE VARIATION: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    Time: O(n^2) TIME LIMIT EXCEEDED ON LEETCODE
    Space: O(1) 
    """

    # Profit = p[k] - p[i] where: k = sell day,  i = buy day
    max_profit = 0
    for i in range(len(p)-1):
        for k in range(i, len(p)):
            if p[k] - p[i] >= max_profit:
                max_profit = p[k] - p[i]

    return max_profit


def custom_buy_and_sell_stock_once(prices):
    """
    Accepted on Leetcode
    Time: O(n) 
    Space: O(1) 
    """

    max_profit = 0
    current_lowest = 0

    i = 0
    while i < len(prices) - 1:
        if prices[current_lowest] > prices[i + 1]:
            current_lowest += (i-current_lowest+1)
            i += 1
        else:
            i += 1
            if prices[i] - prices[current_lowest] > max_profit:
                max_profit = prices[i] - prices[current_lowest]

    return max_profit


def buy_and_sell_stock_once(prices):
    """
    EPI Solution
    Time: O(n) 
    Space: O(1) 
    """

    max_profit = 0.0
    min_price_so_far = float('inf')
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit


print(buy_and_sell_stock_once(
    [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
