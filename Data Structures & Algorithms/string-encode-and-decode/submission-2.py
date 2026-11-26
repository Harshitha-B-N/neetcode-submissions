class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            sep = s.find("#", i)
            length = int(s[i:sep])
            res.append(s[sep + 1 : sep + 1 + length])
            i = sep + 1 + length
        return res