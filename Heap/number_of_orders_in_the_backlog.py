import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buys = []
        sells = []
        for price, amount, order_type in orders:
            if order_type == 0:  # buy
                heapq.heappush(buys, [-price, amount])
            else:  # sell
                heapq.heappush(sells, [price, amount])
            while buys and sells and -buys[0][0] >= sells[0][0]:
                deal = min(buys[0][1], sells[0][1])
                buys[0][1] -= deal
                sells[0][1] -= deal
                if buys[0][1] == 0:
                    heapq.heappop(buys)
                if sells[0][1] == 0:
                    heapq.heappop(sells)
        return sum(amount for price, amount in buys + sells) % (10 ** 9 + 7)
