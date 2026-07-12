class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        p = []
        for token in tokens:
        
            if token not in "+-*/":
                p.append(token)
            else:
                b = p.pop()
                a = p.pop()
                if token == "/":
                    res = int(a) // int(b)
                    res = res if res >= 0 or int(a)/int(b) % 1 == 0 else res + 1
                    p.append(res)
                else:
                    p.append(eval(str(a)+token+str(b)))
        return int(p.pop())