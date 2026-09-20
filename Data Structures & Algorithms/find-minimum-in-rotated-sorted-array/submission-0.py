class Solution:
    def findMin(self, nums: List[int]) -> int:
        k_min, k_max = 0, len(nums) - 1
        while k_min <= k_max:
            k_mid = (k_min + k_max) // 2
            first = nums[k_min]
            last = nums[k_max]
            medium = nums[k_mid]
            # print(k_min, k_mid, k_max, first, medium, last)
            # print(medium < first, medium > last)
            if medium < first: 
                k_max = k_mid
            elif medium > last:
                k_min = k_mid + 1
            else: 
                break
        return nums[k_min]





