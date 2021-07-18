from re import search


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        if not brokenLetters:
            return text.count(' ') + 1
        return sum(not search(f'[{brokenLetters}]', word)
                   for word in text.split())
