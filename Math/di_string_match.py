class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        perm = [0] * (len(S) + 1)
        low, high = 0, len(S)
        for i, c in enumerate(S):
            if c == 'I':
                perm[i] = low
                low += 1
            else:
                perm[i] = high
                high -= 1
        perm[-1] = low
        return perm
