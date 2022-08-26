from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_list = []
        arr_len = 0
        for idx, a in enumerate(arr):
            if a == 0:
                zero_list.append(idx)
            arr_len += 1
        for i in zero_list:
            idx = zero_list.pop(0)
            arr.insert(idx, 0)
            zero_list = [ele + 1 for ele in zero_list]
        print(arr_len)

        arr = arr[0:arr_len]

class OptimalSolution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_cnt = 0
        arr_len = len(arr)
        # arr_len = 0
        for idx, a in enumerate(arr):
            if a == 0:
                zero_cnt += 1

        for i in range(arr_len-1, -1, -1):
            # shift the current element by its current position with the number of zeros
            if i + zero_cnt < arr_len:
                arr[i+zero_cnt] = arr[i]
            # duplicate the zeros
            if arr[i] == 0:
                zero_cnt -= 1
                if i + zero_cnt < arr_len:
                    print(i, i+zero_cnt)
                    arr[i+zero_cnt] = 0


optimal_sol = OptimalSolution()
arr = [1,0,2,3,0,4,5,0]
optimal_sol.duplicateZeros(arr)