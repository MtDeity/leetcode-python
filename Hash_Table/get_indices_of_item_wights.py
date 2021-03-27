from typing import List, Dict, Tuple
import unittest


def get_indices_of_item_wights(arr: List[int], limit: int) -> List[int]:
    if len(arr) < 2:
        return []

    diff_indices: Dict[int, int] = {}
    for index, weight in enumerate(arr):
        if weight in diff_indices:
            diff_index = diff_indices[weight]
            return [index, diff_index]
        diff = limit - weight
        diff_indices[diff] = index
    return []


class Test(unittest.TestCase):
    test_cases: List[Tuple[List[int], int, List[int]]] = [
        ([9], 9, []),
        ([4, 4], 8, [1, 0]),
        ([4, 4, 1], 5, [2, 1]),
        ([4, 6, 10, 15, 16], 21, [3, 1]),
        ([4, 6, 10, 15, 16], 20, [4, 0]),
        ([12, 6, 7, 14, 19, 3, 0, 25, 40], 7, [6, 2]),
    ]

    def test_get_indices_of_item_wights(self):
        for arr, limit, expected in self.test_cases:
            actual = get_indices_of_item_wights(arr, limit)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
