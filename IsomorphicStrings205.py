class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        vals = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in vals:
                if t[i] in used:
                    return False
                vals[s[i]] = t[i]
                used.add(t[i])
            if vals[s[i]] != t[i]:
                return False
        return True