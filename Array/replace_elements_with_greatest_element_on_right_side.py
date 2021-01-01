class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_el = -1
        for i in reversed(range(len(arr))):
            arr[i], max_el = max_el, max(max_el, arr[i])
        return arr
