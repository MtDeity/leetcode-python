class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        lgth = len(arr)
        for i in range(lgth - 2):
            for j in range(i + 1, lgth - 1):
                if not abs(arr[i] - arr[j]) <= a:
                    continue
                for k in range(j + 1, lgth):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count
