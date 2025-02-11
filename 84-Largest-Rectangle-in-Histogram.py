class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0
        for i, h in enumerate(heights):
            while len(stack) > 1 and stack[-1] != -1 and h <= heights[stack[-1]]:
                st_top = stack.pop()
                curr_area = heights[st_top] * (i - stack[-1] - 1)
                ans = max(curr_area, ans)
            stack.append(i)
        
        while len(stack) > 1 and stack[-1] != -1:
            st_top = stack.pop()
            curr_area = heights[st_top] * (len(heights)-stack[-1]-1)
            ans = max(curr_area, ans)
        return ans


                
        