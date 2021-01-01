class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        length = len(A)
        left = 0
        right = length - 1
        while left < right:
            while left < length and A[left] % 2 == 0:
                left += 1
            while right > 0 and A[right] % 2 == 1:
                right -= 1
            if left < right:
                A[left], A[right] = A[right], A[left]
        return A
