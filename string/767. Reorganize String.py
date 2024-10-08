from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        q = []
        heapq.heapify(q)

        for s_, c_ in c.items():
            heapq.heappush(q, (c_ * -1, s_))

        ans = ""
        prev = None

        while q or prev:
            if prev and not q:
                return ""

            cnt, curr_s = heapq.heappop(q)
            cnt += 1
            ans += curr_s

            if prev:
                heapq.heappush(q, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, curr_s)

        return ans


sol = Solution()
sol.reorganizeString("aab")
