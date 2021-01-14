class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first] + encoded
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        return arr
