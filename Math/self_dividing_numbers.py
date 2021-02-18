class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if self.selfDividingNumber(i)]

    def selfDividingNumber(self, num: int) -> bool:
        num_str = str(num)
        for c in num_str:
            if c is '0' or num % int(c) != 0:
                return False
        return True
