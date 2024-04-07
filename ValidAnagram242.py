class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in countS:
                countS[s[i]] = 1
            else:
                countS[s[i]] += 1
            if t[i] not in countT:
                countT[t[i]] = 1
            else:
                countT[t[i]] += 1
        for k in countS:
            if k not in countS or k not in countT:
                return False
            elif countS[k] != countT[k]:
                return False
        return True