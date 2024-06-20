class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hMap = {'b': 0, 'a': 0, 'l': 0, 'o':0, 'n':0}
        for i in text:
            if i not in hMap:
                continue
            else:
                hMap[i] += 1
                
        minCount = float('inf')

        for j in hMap.keys():
            if j == 'l' or j == 'o':
                minCount = min(minCount, hMap[j]//2)
            else:
                minCount = min(minCount, hMap[j])
        return minCount
