class Solution:
    def twoOutOfThree(
            self,
            nums1: list[int],
            nums2: list[int],
            nums3: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        res: list[int] = []
        for i in range(1, 101):
            if (i in s1) + (i in s2) + (i in s3) >= 2:
                res.append(i)
        return res
