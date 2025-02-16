class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_swap_idx = second_swap_idx = num_diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diff += 1

                if num_diff > 2:
                    return False 
                
                if num_diff == 1:
                    first_swap_idx = i
                else:
                    second_swap_idx = i
                    


        return s1[first_swap_idx] == s2[second_swap_idx] and s1[second_swap_idx] == s2[first_swap_idx]
        
        