class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) <= 0:
            return 0

        num = start = 0
        sign = 1
        if s[0] == '+':
            start += 1
        elif s[0] == '-':
            sign = -1
            start += 1

        nums = '0123456789'
        for c in s[start:]:
            if c not in nums:
                break
            num = num * 10 + int(c)
        num *= sign

        if num < -2 ** 31:
            num = -2 ** 31
        elif num > 2 ** 31 - 1:
            num = 2 ** 31 - 1
        return num
