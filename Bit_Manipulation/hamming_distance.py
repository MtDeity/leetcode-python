class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return bin(x^y).count('1')
        xor = x ^ y
        distance = 0
        while xor:
            xor &= xor - 1
            distance += 1
        return distance
