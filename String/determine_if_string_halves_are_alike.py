class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        half = len(s) // 2
        a = s[:half]
        b = s[half:]

        a_map = {}
        b_map = {}
        for c in a:
            a_map[c] = a_map[c] + 1 if c in a_map else 1
        for c in b:
            b_map[c] = b_map[c] + 1 if c in b_map else 1

        a_count = b_count = 0
        for vowel in vowels:
            if vowel in a_map:
                a_count += a_map[vowel]
            if vowel in b_map:
                b_count += b_map[vowel]

        return a_count == b_count
