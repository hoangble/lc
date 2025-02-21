from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = defaultdict(list)
        for key, cnt in counter.items():
            freq[cnt].append(key)

        res = []
        for times in range(len(nums) + 1, -1, -1):
            if times in freq:
                res.extend(freq[times])
            if len(res) >= k:
                return res[:k]
        return res[:k]


Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
