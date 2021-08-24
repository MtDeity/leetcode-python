class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1 = int(num1.split('+')[0])
        i1 = int(num1.split('+')[1][:-1])
        r2 = int(num2.split('+')[0])
        i2 = int(num2.split('+')[1][:-1])
        return f'{r1 * r2 - i1 * i2}+{r1 * i2 + r2 * i1}i'
