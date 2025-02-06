class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        curr_max = 0
        ans = []
        # for i in range(len(heights) -1, -1, -1):
            # if heights[i] > curr_max:
                # curr_max = heights[i]
                # ans.append(i)

        # return ans[::-1] 

        # iterate from left to right, e.g. streaming
        for i, h in enumerate(heights):
            while ans and heights[ans[-1]] <= h:
                ans.pop()
            ans.append(i)
        return ans