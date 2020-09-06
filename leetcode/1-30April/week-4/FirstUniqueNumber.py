class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.has = {}
        self.pointer = 0

        for i, n in enumerate(nums):
            currentCount = 0 if self.has.get(n) == None else self.has[n]
            self.has[n] = currentCount + 1

    def showFirstUnique(self) -> int:
        for i in range(self.pointer, len(self.nums)):
            if self.has[self.nums[i]] == 1:
                return self.nums[i]
            self.pointer = i
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        currentCount = 0 if self.has.get(value) == None else self.has[value]
        self.has[value] = currentCount + 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
