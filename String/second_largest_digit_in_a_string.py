class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        largest2 = -1
        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                number = int(c)
                if number > largest:
                    largest, largest2 = number, largest
                elif largest > number > largest2:
                    largest2 = number
        return largest2
