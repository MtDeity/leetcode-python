from typing import List


class Solution:
    def matrixReshape(self,
                      mat: List[List[int]],
                      r: int,
                      c: int) -> List[List[int]]:
        ans = [num for row in mat for num in row]
        if len(ans) != r * c:
            return mat
        return [ans[i * c:(i + 1) * c] for i in range(r)]
