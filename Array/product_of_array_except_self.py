class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Left and Right product lists
        # length = len(nums)
        # left = [0]*length
        # right = [0]*length
        # ans = [0]*length
        # left[0] = 1
        # for i in range(1, length):
        #     left[i] = left[i - 1] * nums[i - 1]
        # right[length - 1] = 1
        # for i in reversed(range(length - 1)):
        #     right[i] = right[i + 1] * nums[i + 1]
        # for i in range(length):
        #     ans[i] = left[i] * right[i]
        # return ans

        # O(1) space approach
        length = len(nums)
        ans = [0]*length
        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
        for i in reversed(range(length)):
            ans[i] = ans[i] * right
            right *= nums[i]
        return ans
