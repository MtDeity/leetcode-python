class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i + 1 for i in range(n)]
        length = n
        index = skip = k - 1
        while length > 1:
            circle.pop(index)
            length -= 1
            index = (index + skip) % length
        return circle[0]
