class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        best_single_start = 0
        best_double_start = [0, k]
        best_triple_start = [0, k, k*2]

        first_window_sum = sum(nums[:k])
        second_window_sum = sum(nums[k:k*2])
        third_window_sum = sum(nums[k*2 : k * 3])

        best_single_sum = first_window_sum
        best_double_sum = best_single_sum + second_window_sum
        best_triple_sum = best_double_sum + third_window_sum

        start_first_idx = 1
        start_second_idx = k + 1
        start_third_idx = k * 2 + 1
        
        while start_third_idx <= len(nums) - k:
            first_window_sum = first_window_sum - nums[start_first_idx - 1] + nums[k + start_first_idx - 1]
            if first_window_sum > best_single_sum:
                best_single_start = start_first_idx
                best_single_sum = first_window_sum
            
            second_window_sum = second_window_sum - nums[start_second_idx - 1] + nums[k + start_second_idx - 1]
            if second_window_sum + best_single_sum > best_double_sum:
                best_double_start[0] = best_single_start
                best_double_start[1] = start_second_idx
                best_double_sum = second_window_sum + best_single_sum


            third_window_sum = third_window_sum - nums[start_third_idx - 1] + nums[k + start_third_idx - 1]
            if third_window_sum + best_double_sum > best_triple_sum:
                best_triple_start[0] = best_double_start[0]
                best_triple_start[1] = best_double_start[1]
                best_triple_start[2] = start_third_idx
                best_triple_sum = third_window_sum + best_double_sum

            start_first_idx += 1
            start_second_idx += 1
            start_third_idx += 1

        return best_triple_start 



