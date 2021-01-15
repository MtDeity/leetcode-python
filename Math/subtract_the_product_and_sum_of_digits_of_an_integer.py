class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summation = 0
        while n > 0:
            module = n % 10
            product *= module
            summation += module
            n //= 10
        return product - summation
