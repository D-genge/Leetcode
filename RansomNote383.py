class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for i in magazine:
            if i not in mag:
                mag[i] = 1
            else:
                mag[i] += 1
        
        for i in ransomNote:
            if i not in mag:
                return False
            elif mag[i] <= 0:
                return False
            else:
                mag[i] -= 1
        return True
        
