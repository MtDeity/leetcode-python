class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # for i in range(len(prices)):
        #     discount = 0
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] <= prices[i]:
        #             discount = prices[j]
        #             break
        #     prices[i] -= discount
        # return prices
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
        return prices
