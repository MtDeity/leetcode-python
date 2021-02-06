class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path_set = set(path[0] for path in paths)
        for path in paths:
            if not path[1] in path_set:
                return path[1]
