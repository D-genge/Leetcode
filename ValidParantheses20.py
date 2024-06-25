class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {']': '[', '}':'{', ')': '('}
        stack = []
        for i in range(len(s)):
            if s[i] not in pMap: # If open brace
                stack.append(s[i]) 
            elif s[i] in pMap:
                if len(stack) >= 1 and pMap[s[i]] == stack.pop():
                    continue
                else:
                    return False
        return not stack
