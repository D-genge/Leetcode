class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def backTrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in hmap[digits[i]]:
                backTrack(i+1, curStr + c)
        backTrack(0, "")
        return res if res != [""] else []