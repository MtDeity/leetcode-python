class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        length = len(s)
        a = b = i = 0
        j = length // 2

        while j < length:
            a += 1 if s[i] in vowels else 0
            b += 1 if s[j] in vowels else 0
            i += 1
            j += 1

        return a == b
