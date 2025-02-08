class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {\digit\: 1, \sign\: 2, \dot\: 3},
            {\digit\: 1, \dot\: 4, \exponent\: 5},
            {\digit\: 1, \dot\: 3},
            {\digit\: 4},
            {\digit\: 4, \exponent\: 5},
            {\sign\: 6, \digit\: 7},
            {\digit\: 7},
            {\digit\: 7},
        ]

        curr = 0
        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                group = 'digit'
            elif c == 'E' or c == 'e':
                group = 'exponent'
            elif c == '.':
                group = 'dot'
            elif c == '-' or c == '+':
                group = 'sign'
            else:
                return False
        
            if group not in states[curr]:
                return False
            curr = states[curr][group]
        return curr in set([1, 4, 7])
            