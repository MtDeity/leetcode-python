class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = list(s)
        left = 0
        right = len(letters) - 1
        while left < right:
            if not letters[left].isalpha():
                left += 1
            elif not letters[right].isalpha():
                right -= 1
            else:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1
        return ''.join(letters)
