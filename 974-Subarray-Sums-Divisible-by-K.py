class Solution:
    from collections import defaultdict
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        hash_map = defaultdict(int)
        hash_map[0] = 1
        sum_ = 0
        for n in nums:
            sum_ += n 
            ans += hash_map[sum_%k]
            hash_map[sum_%k] += 1
        return ans