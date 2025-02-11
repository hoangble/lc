class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []

        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.popleft()
            q.append(i)
        
        res.append(nums[q[-1]])

        for i in range(k, len(nums))
