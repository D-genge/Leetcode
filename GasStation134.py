class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        curGas = 0
        start = 0
        for i in range(n):
            curGas += gas[i] - cost[i]
            if curGas < 0:
                curGas = 0
                start = i + 1
        return start
