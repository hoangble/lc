from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        st = []
        res = [0] * len(heights)
        for i, h in enumerate(heights):
            while st and heights[st[-1]] <= h:
                res[st.pop()] += 1
            if st:
                res[st[-1]] += 1
            st.append(i)
        return res


sol = Solution()
sol.canSeePersonsCount([10, 6, 8, 5, 11, 9])
