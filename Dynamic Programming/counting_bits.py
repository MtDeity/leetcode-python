from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [-1] * (n + 1)
        ans[0] = 0
        for i in range(1, n + 1):
            if i % 2 != 0:
                ans[i] = ans[i - 1] + 1
            else:
                ans[i] = ans[i // 2]
        return ans
