# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/ 
# 1151. Minimum Swaps to Group All 1's Together


from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total_ones = sum(data)
        # print(total_ones)
        total_zeros = len(data) - sum(data)
        
        if total_ones == 1 or total_ones == len(data) or total_zeros == len(data): return 0

        left, right = 0, 0
        # zeros_cnt = 0
        # ones_cnt = 0
        
        n_swap = 0
        min_n_swap = float('inf')
        
        while right < len(data):
            if data[right] == 0:
                n_swap += 1
                
            while right - left + 1 > total_ones and left < right:
                if data[left] == 0:
                    n_swap -= 1
                left += 1
            
            if right - left + 1 == total_ones:
                min_n_swap = min(min_n_swap, n_swap)
                # print(min_n_swap)
            # print(n_swap)
            right += 1            
            
        return min_n_swap

if __name__ == "__main__":
    sol = Solution()
    data = [1,0,1,0,1]
    sol.minSwaps(data)

#%%
ord("B")
# ord("b")
