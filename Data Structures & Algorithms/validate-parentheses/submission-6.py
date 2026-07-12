class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        comb = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for i in s:
            if i in "({[":
                p.append(i)
            else:
                if len(p) == 0: return False
                c = comb[p.pop()]
                if c != i: return False
        return len(p) == 0
        