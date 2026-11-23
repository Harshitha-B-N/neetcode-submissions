from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = Counter(s)
        t_ = Counter(t)
        if s_ == t_:
            return True
        else:
            return False
        