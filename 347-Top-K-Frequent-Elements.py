class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = defaultdict(list)
        for key, cnt in counter.items():
            freq[cnt].append(key)
        
        res = []
        for times in range(len(nums) + 1 , -1, -1):
            res.extend(freq[times])
            if len(res) >= k:
                return res[:k]
        return res[:k]
        