class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        d = {}
        js = {}
        for i, e in enumerate(nums):
            d[e] = i
            js[e] = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                if i>1 and nums[i] == nums[i-1]:
                    continue
                if ((-nums[i] - nums[j] in d) 
                    and (d[-nums[i] - nums[j]] > j)
                    and (nums[j] not in js.get(-nums[i] - nums[j]))
                        ):
                    js[-nums[i] - nums[j]].append(nums[j])
                    res.append([nums[i], nums[j], -nums[i] - nums[j]])
        return res