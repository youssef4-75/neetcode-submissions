class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if target <= 0 or nums == []:
            return []
        if target<nums[0]: return []
        if target == nums[0]: return [[nums[0]]]
        res = []
        A = self.combinationSum(nums, target-nums[0])
        for a in A:
            res.append([nums[0]] + a)
        B = self.combinationSum(nums[1:], target)
        for b in B:
            res.append(b)
        return res

            