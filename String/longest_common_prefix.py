from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        i = len(strs[0])
        for word in strs[1:]:
            while(prefix != word[0:i]):
                prefix = prefix[0:(i - 1)]
                i -= 1
                if i == 0:
                    return ""
        return prefix
