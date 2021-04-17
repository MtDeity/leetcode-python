from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n: int = len(nums)
        k %= n
        start_idx: int = 0
        count: int = 0
        while count < n:
            cur_idx, prev = start_idx, nums[start_idx]
            while True:
                next_idx = (cur_idx + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                cur_idx = next_idx
                count += 1
                if start_idx == cur_idx:
                    break
            start_idx += 1

    #     self.reverse(nums, 0, length - 1)
    #     self.reverse(nums, 0, k - 1)
    #     self.reverse(nums, k, length - 1)

    # def reverse(self, nums: List[int], start: int, end: int) -> None:
    #     if start >= end:
    #         return
    #     while start < end:
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1
