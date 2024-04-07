class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        vals = {}
        used = set()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in vals:
                if words[i] in used:
                    return False
                vals[pattern[i]] = words[i]
                used.add(words[i])
            elif vals[pattern[i]] != words[i]:
                return False
        return True