def get_reference_solution(title):

    solutions = {

        "Best Time to Buy and Sell Stock": {
            "approach": "Track minimum price and calculate max profit in one pass",
            "code": """def max_profit(prices):
    min_price = float('inf')
    profit = 0

    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)

    return profit"""
        },

        "Two Sum": {
            "approach": "Use hashmap to store complements",
            "code": """def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i"""
        },

        "Reverse String": {
            "approach": "Use slicing or two pointers",
            "code": """def reverse_string(s):
    return s[::-1]"""
        }
    }

    return solutions.get(title, {
        "approach": "No reference available",
        "code": "Not available"
    })