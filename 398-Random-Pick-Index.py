class Solution:

    def __init__(self, nums: List[int]):
        self.d = {}
        for i in range(len(nums)):
            if nums[i] not in self.d:
                self.d[nums[i]] = []
            self.d[nums[i]].append(i)

    def pick(self, target: int) -> int:
        # size = len(self.d[target])
        return random.choice(self.d[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)