class Solution:
    def trap(self, height: List[int]) -> int:
        # stack = []
        # ans = 0
        # for i, h in enumerate(height):
        #     while stack and h > height[stack[-1]]:
        #         stack_top = stack.pop()
        #         if not stack: break
        #         distance = i - stack[-1] - 1
        #         bounded_height = min(h, height[stack[-1]]) - height[stack_top]
        #         ans += bounded_height * distance
        #     stack.append(i)
        # return ans 
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                ans += right_max - height[right]
                right -= 1
        return ans