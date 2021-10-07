class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.search(board, word, x, y, 0):
                    return True
        return False

    def search(self,
               board: list[list[str]],
               word: str,
               x: int,
               y: int,
               i: int) -> bool:
        if i == len(word):
            return True
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False
        if board[x][y] != word[i]:
            return False
        board[x][y], tmp = '#', board[x][y]
        res = self.search(board, word, x - 1, y, i + 1) \
            or self.search(board, word, x + 1, y, i + 1) \
            or self.search(board, word, x, y - 1, i + 1) \
            or self.search(board, word, x, y + 1, i + 1)
        board[x][y] = tmp
        return res
