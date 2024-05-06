class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word not in hmap:
                curList = []
                curList.append(strs[i])
                hmap[word] = curList
            else:
                curList = hmap[word]
                curList.append(strs[i])
                hmap[word] = curList
        res = []
        for val in hmap.keys():
            res.append(hmap[val])
        return res
