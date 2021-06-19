class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return str(n)
        return self.say(self.countAndSay(n - 1))

    def say(self, s: str) -> str:
        res = ''
        cur = s[0]
        i = 1
        for c in s[1:]:
            if c == cur:
                i += 1
            else:
                res += str(i) + cur
                cur = c
                i = 1
        res += str(i) + cur
        return res
