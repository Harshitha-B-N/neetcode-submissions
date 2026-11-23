class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, i in enumerate(nums):
            expected = target - i
            if expected in seen:
                return [seen[expected], idx]
            seen[i] = idx
        