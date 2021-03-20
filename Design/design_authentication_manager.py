class AuthenticationManager:

    def __init__(self, time_to_live: int):
        self.time_to_live = time_to_live
        self.tokens = {}

    def generate(self, token_id: str, current_time: int) -> None:
        self.tokens[token_id] = current_time + self.time_to_live

    def renew(self, token_id: str, current_time: int) -> None:
        if not token_id in self.tokens:
            return
        if self.tokens[token_id] <= current_time:
            return
        self.tokens[token_id] = current_time + self.time_to_live

    def countUnexpiredTokens(self, current_time: int) -> int:
        return sum([time > current_time for time in self.tokens.values()])

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
