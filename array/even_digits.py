from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            even = True
            while num >= 1:
                num /= 10
                even = not even
            if even:
                cnt += 1
        return cnt


## cleaner solution
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = [str(x) for x in nums]
        c = 0
        for i in l:
            if (
                len(i) & 1
            ):  ## instead of divide by 2, do a bitwise and to check if # digits is odd
                c += 1
        return len(l) - c  ## n_even_num = total - odds


# %%
arr = [1, 0, 2, 3, 0, 4, 5, 0]
i = 0
for element in arr:
    if element == 0:
        arr.insert(i, element)
        i += 1
        print(i)
        print(arr)

    i += 1
print(arr)

# %%
