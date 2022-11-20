class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.get_pairs([], n, n, ans)
        return ans
    
    def get_pairs(self, gen_pair, avail_open, avail_close, ans):          
        if avail_open == 0 and avail_close == 0:
            ans.append("".join(gen_pair))
            return
        
        if avail_open > 0:
            gen_pair.append("(")
            self.get_pairs(gen_pair, avail_open - 1, avail_close, ans)
            gen_pair.pop()
        
        if avail_open < avail_close and avail_close > 0:
            gen_pair.append(")")
            self.get_pairs(gen_pair, avail_open, avail_close - 1, ans)
            gen_pair.pop()
        
        
        
        
        
            
            
        