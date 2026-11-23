from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = Counter(s)
        t_ = Counter(t)
        return s_ == t_