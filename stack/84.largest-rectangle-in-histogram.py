from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        ans = 0
        for i in range(len(heights)):
            while st[-1] != -1 and heights[i] <= heights[st[-1]]:
                h = heights[st.pop()]
                w = i - st[-1] - 1
                ans = max(ans, h * w)
            st.append(i)

        while st[-1] != -1:
            h = heights[st.pop()]
            w = len(heights) - st[-1] - 1
            ans = max(ans, h * w)
        return ans


Solution().largestRectangleArea([2, 1, 3, 2])
