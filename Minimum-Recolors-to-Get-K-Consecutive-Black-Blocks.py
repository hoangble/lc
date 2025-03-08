class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # find a min # "W" within k-length window

        w = 0
        for i in range(k):
            w += blocks[i] == 'W'

        ans = w
        for i in range(k, len(blocks)):
            w -= blocks[i - k] == 'W'
            w += blocks[i] == 'W'
            ans = min(ans, w)
        
        return ans