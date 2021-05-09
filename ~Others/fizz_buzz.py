from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res: List[str] = [''] * n
        i: int = 1
        three: int = 3
        five: int = 5
        while i <= n:
            if i == three and i == five:
                res[i - 1] = 'FizzBuzz'
                three += 3
                five += 5
            elif i == three:
                res[i - 1] = 'Fizz'
                three += 3
            elif i == five:
                res[i - 1] = 'Buzz'
                five += 5
            else:
                res[i - 1] = str(i)
            i += 1
        return res
