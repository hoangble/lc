class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = [0] * 1001
        for n in arr1:
            cnt[n] += 1
        
        result = []
        for n in arr2:
            while cnt[n] > 0:
                result.append(n)
                cnt[n] -= 1
        
        for i in range(1001):
            while cnt[i] > 0:
                result.append(i)
                cnt[i] -= 1
        return result
