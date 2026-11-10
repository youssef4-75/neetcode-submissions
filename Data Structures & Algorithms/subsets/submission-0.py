class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for e in nums:
            res = res + [i+[e] for i in res]
        return res
        