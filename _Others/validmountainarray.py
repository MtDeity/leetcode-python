class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        is_decreasing = False
        for i in range(len(arr) - 1):
            if arr[0] >= arr[1]:
                return False
            if arr[i] == arr[i + 1]:
                return False
            if not is_decreasing:
                if arr[i] > arr[i + 1]:
                    is_decreasing = True
            else:
                if arr[i] <= arr[i + 1]:
                    return False
        return is_decreasing
