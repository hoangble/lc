from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        all_triplets = set()
        for end in range(len(nums)):
            i = 0
            j = end - 1
            while i < j:
                if nums[i] + nums[j] + nums[end] < target:
                    all_triplets.add((nums[i], nums[j], nums[end]))
                    i += 1
                else:
                    j -= 1
        print(all_triplets)
        return len(all_triplets)


Solution().threeSumSmaller([-2, 0, 1, 3], 2)
