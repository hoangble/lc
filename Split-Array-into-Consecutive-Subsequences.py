class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        subsequences = defaultdict(int)

        for n in nums:
            if freq[n] == 0:
                continue
            
            if subsequences[n-1] > 0:
                subsequences[n-1] -= 1
                subsequences[n] += 1
            elif freq[n+1] > 0 and freq[n+2] > 0:
                subsequences[n+2] += 1
                freq[n+1] -= 1
                freq[n+2] -= 1
            else:
                return False
            
            freq[n] -= 1
        return True