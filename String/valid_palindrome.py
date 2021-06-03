from re import sub


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = sub('[^a-z0-9]', '', s.lower())
        return s == s[::-1]
