class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')
        for p in parts:
            if len(p) == 0 or p == '.':
                continue
            
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return '/' + '/'.join(stack)

