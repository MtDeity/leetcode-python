from typing import Set


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers: Set[int] = set()
        current_number: str = ''
        for i, char in enumerate(word):
            if ord('0') <= ord(char) <= ord('9'):
                current_number += char
            if current_number:
                if i == len(word) - 1 \
                        or (ord(char) < ord('0') or ord(char) > ord('9')):
                    numbers.add(int(current_number))
                    current_number = ''
        return len(numbers)
