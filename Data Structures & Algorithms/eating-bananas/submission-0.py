class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles)  # 4
        k_min = 0  # 0
        while k_max > k_min: #
            k = (k_max + k_min) // 2  # 12 19 22 24
            # 2+1+2+1 = 
            c_h = 0 
            for bananas in piles:
                if k == 0:
                    c_h = float("inf")
                    break
                c_h += bananas // k  # 
                if bananas % k != 0:  # 
                    c_h += 1  # 
            # ch = 6
            if c_h > h:  
                k_min = k + 1 # 13 20 23 25
            elif c_h <= h:  # 
                k_max = k
        
        return k_max