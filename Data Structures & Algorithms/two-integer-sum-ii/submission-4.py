class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        s = numbers[left] + numbers[right]
        while s != target:
            if s < target:
                left += 1
            else:
                right -= 1
            s = numbers[left] + numbers[right]
        return [left+1, right+1]
