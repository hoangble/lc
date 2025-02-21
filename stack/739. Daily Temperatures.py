from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # st = []
        # ans = [0] * len(temperatures)
        # for i, t in enumerate(temperatures):
        #     while st and t > temperatures[st[-1]]:
        #         ans[st[-1]] = i - st[-1]
        #         st.pop()
        #     st.append(i)
        # return ans

        ans = [0] * len(temperatures)
        hottest = 0
        for curr_day in range(len(temperatures) - 1, -1, -1):
            curr = temperatures[curr_day]
            if curr >= hottest:
                hottest = curr
                continue

            days = 1
            while temperatures[days + curr_day] <= curr:
                days += ans[days + curr_day]
            ans[curr_day] = days
        return ans


Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
