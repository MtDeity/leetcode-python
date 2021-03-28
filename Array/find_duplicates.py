from typing import List, Tuple
import unittest


def find_duplicates(arr1: List[int], arr2: List[int]) -> List[int]:
    i: int = 0
    j: int = 0
    duplicates: List[int] = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            duplicates.append(arr1[i])
            i += 1
            j += 1
    return duplicates


class Test(unittest.TestCase):
    test_cases: List[Tuple[List[int], List[int], List[int]]] = [
        ([11], [11], [11]),
        ([1, 3, 5, 9], [2, 4, 6, 10], []),
        ([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20], [3, 6, 7]),
        ([1, 2, 3, 5, 6, 7], [7, 8, 9, 10, 11, 12], [7]),
        (
            [10, 20, 30, 40, 50, 60, 70, 80],
            [10, 20, 30, 40, 50, 60],
            [10, 20, 30, 40, 50, 60]
        ),
        (
            [10, 20, 30, 40, 50, 60, 70],
            [10, 20, 30, 40, 50, 60, 70],
            [10, 20, 30, 40, 50, 60, 70]
        ),
    ]

    def test_find_duplicates(self):
        for arr1, arr2, expected in self.test_cases:
            actual = find_duplicates(arr1, arr2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
