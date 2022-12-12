# https://leetcode.com/problems/shortest-path-to-get-all-keys/ 
# 864. Shortest Path to Get All Keys
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # state (have_keys, next_key, curr_pos)