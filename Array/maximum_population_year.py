from typing import List, Tuple


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        changes: List[Tuple[int, int]] = []
        for birth, death in logs:
            changes.append((birth, 1))
            changes.append((death, -1))
        changes.sort()
        max_year = max_population = current_population = 0
        for year, change in changes:
            current_population += change
            if current_population > max_population:
                max_population = current_population
                max_year = year
        return max_year
