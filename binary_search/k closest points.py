from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        all_dist = [self.cal_dist(p) for p in points]
        remaining = [i for i in range(len(points))]

        l, r = 0, max(all_dist)
        closest = []
        while k:
            m = (l + r) / 2
            more, less = self.split(all_dist, remaining, m)

            if len(less) <= k:
                l = m
                k = k - len(less)
                closest.extend(less)
                remaining = more
            else:
                r = m
                remaining = less

        return [points[i] for i in closest]

    def split(self, all_distance, all_idx, m):
        more = []
        less = []
        for i in all_idx:
            if all_distance[i] <= m:
                less.append(i)
            else:
                more.append(i)
        return more, less

    def cal_dist(self, point):
        return point[0] ** 2 + point[1] ** 2


Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
