class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        a: set[int] = set()
        b: set[int] = set()
        for i, move in enumerate(moves):
            if i % 2 == 0:
                a.add(self.to_num(move))
            else:
                b.add(self.to_num(move))
        if self.is_winner(a):
            return "A"
        elif self.is_winner(b):
            return "B"
        else:
            return "Draw" if len(moves) == 9 else "Pending"

    def is_winner(self, pos: set[int]) -> bool:
        return (0 in pos and 1 in pos and 2 in pos) \
            or (3 in pos and 4 in pos and 5 in pos) \
            or (6 in pos and 7 in pos and 8 in pos) \
            or (0 in pos and 3 in pos and 6 in pos) \
            or (1 in pos and 4 in pos and 7 in pos) \
            or (2 in pos and 5 in pos and 8 in pos) \
            or (0 in pos and 4 in pos and 8 in pos) \
            or (2 in pos and 4 in pos and 6 in pos)

    def to_num(self, move: list[int]) -> int:
        return move[0] * 3 + move[1]
