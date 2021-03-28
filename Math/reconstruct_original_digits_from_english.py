from collections import Counter
from typing import Dict


class Solution:
    def originalDigits(self, s: str) -> str:
        chars: Dict[str, int] = Counter(s)
        nums: Dict[int, int] = {num: 0 for num in range(10)}
        nums[0] = chars['z']
        nums[2] = chars['w']
        nums[4] = chars['u']
        nums[6] = chars['x']
        nums[8] = chars['g']
        nums[3] = chars['h'] - nums[8]
        nums[5] = chars['f'] - nums[4]
        nums[7] = chars['s'] - nums[6]
        nums[1] = chars['o'] - nums[0] - nums[2] - nums[4]
        nums[9] = chars['i'] - nums[5] - nums[6] - nums[8]
        return ''.join([str(num) * nums[num] for num in range(10)])
