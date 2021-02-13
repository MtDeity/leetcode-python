class Solution:
    def generateTheString(self, n: int) -> str:
        n_list = ['a'] * n
        if n % 2 == 0:
            n_list[-1] = 'b'
        return ''.join(n_list)
