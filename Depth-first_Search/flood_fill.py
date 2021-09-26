class Solution:
    def floodFill(self,
                  image: list[list[int]],
                  sr: int,
                  sc: int,
                  newColor: int) -> list[list[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        m = len(image)
        n = len(image[0])
        stack = [(sr, sc)]
        while stack:
            x, y = stack.pop()
            image[x][y] = newColor
            if x + 1 < m and image[x + 1][y] == color:
                stack.append((x + 1, y))
            if 0 <= x - 1 and image[x - 1][y] == color:
                stack.append((x - 1, y))
            if y + 1 < n and image[x][y + 1] == color:
                stack.append((x, y + 1))
            if 0 <= y - 1 and image[x][y - 1] == color:
                stack.append((x, y - 1))
        return image
