class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if nums == [] or len(nums) == 1:
            return [[e] for e in nums]
        for i, e in enumerate(nums):
            for permutation in self.permute(nums[:i] + nums[i+1:]):
                res.append([e]+permutation)
        return res
        