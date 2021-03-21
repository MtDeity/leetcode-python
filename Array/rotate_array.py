class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        start_idx = count = 0
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
