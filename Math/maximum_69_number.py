class Solution:
    def maximum69Number(self, num: int) -> int:
        digit = 0
        current_digit = 1
        while num > current_digit:
            if (num // current_digit) % 10 == 6:
                digit = current_digit
            current_digit *= 10
        return num + 3 * digit
