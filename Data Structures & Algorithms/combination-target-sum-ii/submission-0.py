class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if candidates == [] or target < candidates[0]:
            return []
        if candidates[0] == target:
            return [[target]]

        res = []

        for i in self.combinationSum2(candidates[1:], target-candidates[0]):
            res.append(i+[candidates[0]])
        
        k = 1
        for k in range(1, len(candidates)):
            if candidates[k] != candidates[0]:
                break
        for j in self.combinationSum2(candidates[k:], target):
            res.append(j)
        return res