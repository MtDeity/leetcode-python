class Solution:
    def freqAlphabets(self, s: str) -> str:
        return re.sub(r"\d{2}#|\d", lambda x: chr(int(x.group()[:2]) + ord("a") - 1), s)
