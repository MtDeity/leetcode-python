class Solution:
    rule_keys = {'type' : 0, 'color' : 1, 'name' : 2}
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(item[self.rule_keys[ruleKey]] == ruleValue for item in items)
