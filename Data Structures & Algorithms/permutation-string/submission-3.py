class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = self.dictOf(s1)
        n = len(s1)
        m = len(s2)
        if m < n: return False

        d2 = self.dictOf(s2[:n])
        sp = 0
        sn = 0
        for k in d1.keys():
            d1[k] -= d2.get(k, 0)
            sp += max(0, d1.get(k, 0))
            sn += min(0, d1.get(k, 0))
       
        if sp <= 0: return True

        for i in range(m-n):
            # the window is s2[i: n+i]
            # the in: s[n+i]
            # the out: s[i]
            if s2[n+i] in d1:
                if d1[s2[n+i]] > 0: 
                    sp -= 1
                else: 
                    sn += 1
                d1[s2[n+i]] -= 1
            if s2[i] in d1:
                if d1[s2[i]] < 0:
                    sn -= 1
                else: 
                    sp += 1
                d1[s2[i]] += 1
           
            if sp == 0:
                return True
        return False



    def dictOf(self, s: str) -> dict:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        return d
