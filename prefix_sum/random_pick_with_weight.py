class BruteForceSolution:
    def __init__(self, w: List[int]):
        # self.prob = [i/w.sum() for i in w]
        self.w = w
        import time

        seed = int(time.time())
        # duplicate each item by the weight
        self.duplicated_arr = []
        for num, weight in enumerate(w):
            self.duplicated_arr += [num] * weight
        self.max_ = len(self.duplicated_arr) - 1
        self.prev = seed

    def rng(self, prev):
        a = 11
        b = 15
        res = (a * prev + b) % (self.max_ - 0 + 1) + 0
        return res

    def pickIndex(self) -> int:
        idx = self.rng(self.prev)
        self.prev = idx
        return self.duplicated_arr[idx]


class Solution:
    def __init__(self, w: List[int]):
        # self.prob = [i/w.sum() for i in w]
        self.w = [i for i in range(len(w))]
        import random

        self.prefix_sum = []
        self.prefix_sum.append(w[0])
        curr_sum = w[0]
        for i in range(1, len(w)):
            curr_sum += w[i]
            self.prefix_sum.append(curr_sum)

    def find_closest_number(self, arr, r, l, h):
        # essentially binary search
        while l < h:
            mid = (l + h) // 2
            if arr[mid] < r:
                l = mid + 1
            else:
                h = mid

        if arr[l] >= r:
            return l
        else:
            return -1

    def pickIndex(self) -> int:
        r = random.randint(0, self.prefix_sum[-1]) + 1
        idx = self.find_closest_number(self.prefix_sum, r, 0, len(self.prefix_sum) - 1)
        return self.w[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
