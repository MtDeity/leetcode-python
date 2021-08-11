from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        acc = ''
        for word in words:
            acc += word
            if len(acc) > len(s):
                return False
            elif len(acc) == len(s):
                return acc == s
        return False
