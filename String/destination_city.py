class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        path_map = {}
        for city_a, city_b in paths:
            path_map[city_a] = city_b
        current_city = paths[0][0]
        while 1:
            if current_city in path_map:
                current_city = path_map[current_city]
            else:
                break
        return current_city
