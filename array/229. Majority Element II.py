from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # counter = defaultdict(int)
        # for num in nums:
        #     counter[num] += 1
        
        # ans = []
        # n = len(nums)
        # for c, cnt in counter.items():
        #     if cnt > n // 3:
        #         ans.append(c)
        # return ans
        
        # O(1) solution - Boyer-Moore Voting Algorithm
        c0, c1, cnt0, cnt1, = None, None, 0, 0
        for num in nums:
            if num == c0:
                cnt0 += 1
            elif num == c1:
                cnt1 += 1
            elif cnt0 == 0:
                c0 = num
                cnt0 = 1
            elif cnt1 == 0:
                c1 = num
                cnt1 = 1

            else:
                cnt0 -= 1
                cnt1 -= 1
        
        actual_cnt0, actual_cnt1 = 0, 0
        for num in nums:
            if num == c0: actual_cnt0 += 1
            if num == c1: actual_cnt1 += 1
        
        n = len(nums)
        ans = []
        for c, cnt in ((c0, actual_cnt0), (c1, actual_cnt1)):
            if cnt > n // 3:
                ans.append(c)
        return ans

