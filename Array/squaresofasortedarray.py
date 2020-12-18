class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        squares = [0] * length
        left = 0
        right = length - 1
        for i in reversed(range(length)):
            if abs(nums[left]) > abs(nums[right]):
                squares[i] = nums[left] * nums[left]
                left += 1
            else:
                squares[i] = nums[right] * nums[right]
                right -= 1
        return squares
