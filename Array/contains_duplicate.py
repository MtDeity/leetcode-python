from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st: Set[int] = set()
        for num in nums:
            if num in st:
                return True
            st.add(num)
        return False
