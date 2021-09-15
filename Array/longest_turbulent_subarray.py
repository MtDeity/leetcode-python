class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        cnt = mx = 1
        diff = 0
        for i, n in enumerate(arr[1:]):
            if n == arr[i]:
                cnt = 1
            elif (i == 0) or (diff == 0) or (diff > 0 and n < arr[i]) or (diff < 0 and n > arr[i]):
                cnt += 1
                mx = max(mx, cnt)
            else:
                cnt = 2
            diff = n - arr[i]
        return mx
