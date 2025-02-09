class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                stack_top = stack.pop()
                if not stack: break
                distance = i - stack[-1] - 1
                bounded_height = min(h, height[stack[-1]]) - height[stack_top]
                ans += bounded_height * distance
            stack.append(i)
        return ans 