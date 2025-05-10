from collections import Counter
from typing import List


def minSum(nums1: List[int], nums2: List[int]) -> int:
    counter1 = Counter(nums1)
    sum1 = sum(nums1)
    potential_sum1 = sum1
    if 0 in counter1:
        potential_sum1 += counter1[0]

    sum2 = sum(nums2)
    counter2 = Counter(nums2)
    potential_sum2 = sum2
    if 0 in counter2:
        potential_sum2 += counter2[0]

    if potential_sum1 == potential_sum2:
        return potential_sum1

    if potential_sum1 > potential_sum2:
        if potential_sum2 - sum2 == counter2[0] and counter2[0] != 0:
            return potential_sum1
        else:
            return -1

    if potential_sum1 < potential_sum2:
        if potential_sum1 - sum1 == counter1[0] and counter1[0] != 0:
            return potential_sum2
        else:
            return -1


nums1 = [2, 0, 2, 0]
nums2 = [1, 4]
minSum(nums1, nums2)
