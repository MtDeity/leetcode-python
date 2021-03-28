from typing import Dict, List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_map: Dict[str, str] = {k: v for k, v in knowledge}
        res: str = ''
        current_key: str = ''
        is_key = False
        for char in s:
            if char == '(':
                is_key = True
            elif char == ')':
                is_key = False
                res += knowledge_map.get(current_key, '?')
                current_key = ''
            elif is_key:
                current_key += char
            else:
                res += char
        return res
