class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        char = 'a'
        longest = prev = 0
        for i in range(len(releaseTimes)):
            duration = releaseTimes[i] - prev
            key = keysPressed[i]
            if duration > longest \
                    or (duration == longest and ord(key) >= ord(char)):
                char = key
                longest = duration
            prev = releaseTimes[i]
        return char
