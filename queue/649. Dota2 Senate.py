from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_q = deque([])
        d_q = deque([])

        for i, s in enumerate(senate):
            if s == "R":
                r_q.append(i)
            else:
                d_q.append(i)

        n = len(senate)

        while r_q and d_q:
            r = r_q.popleft()
            d = d_q.popleft()
            if r < d:
                r_q.append(r + n)
            else:
                d_q.append(d + n)
            # i += 1

        if r_q:
            return "Radiant"
        return "Dire"
