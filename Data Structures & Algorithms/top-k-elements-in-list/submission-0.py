from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        result = [i for i, v in sorted(frequency.items(), key=lambda x:x[1], reverse=True)]
        return result[:k]