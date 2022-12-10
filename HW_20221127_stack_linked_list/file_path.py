# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []
        for token in tokens: 
            if stack and token == "..": stack.pop()
            elif token and token != "." and token != "..":
                stack.append(token)
        
        ans = ""
        for token in stack:
            ans += "/" + token 
        
        return ans if ans else "/"