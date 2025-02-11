class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)]
        result = [0] * n

        def merge_sort(arr, l, r):
            if r - l <= 1: return

            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m, r)
            merge(arr, l, r, m)
        
        def merge(arr, l, r, m):
            i = l
            j = m
            tmp = []
            while i < m and j < r:
                if arr[i][0] <= arr[j][0]:
                    result[arr[i][1]] += j - m
                    tmp.append(arr[i])
                    i += 1
                else:
                    tmp.append(arr[j])
                    j += 1
            
            while i < m:
                result[arr[i][1]] += j - m
                tmp.append(arr[i])
                i += 1
            
            while j < r:
                tmp.append(arr[j])
                j += 1
            
            for i in range(l, r):
                arr[i] = tmp[i - l]
        
        
        merge_sort(arr, 0, n)
        return result

