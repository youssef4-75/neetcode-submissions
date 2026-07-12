class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        for i, hi in enumerate(heights):
            for _j, hj in enumerate(heights[i+1:]):
                j = _j + i + 1
                if (j-i)*min(hi, hj) > m:
                    m = (j-i)*min(hi, hj)
        return m