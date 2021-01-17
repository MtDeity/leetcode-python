# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
class OrderedStream:
    def __init__(self, n: int):
        self.list = [""] * n
        self.last = 0

    def insert(self, id: int, value: str) -> List[str]:
        index = id - 1
        self.list[index] = value
        if index > self.last:
            return []
        while self.last < len(self.list) and self.list[self.last]:
            self.last += 1
        return self.list[index: self.last]
