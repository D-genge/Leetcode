class RandomizedSet:

    def __init__(self):
        self.randomSet = {}
        self.randomArray = []

    def insert(self, val: int) -> bool:
        if val not in self.randomSet:
            self.randomArray.append(val)
            self.randomSet[val] = len(self.randomArray) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            endVal = self.randomArray[-1]
            self.randomSet[endVal] = self.randomSet[val]
            self.randomArray[self.randomSet[val]] = endVal
            del self.randomSet[val]
            self.randomArray.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        randNum = random.randint(0, len(self.randomArray) - 1)
        return self.randomArray[randNum]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()