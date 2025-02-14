class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        cnt = 0
        i = 0
        while i < len(abbr):
            if abbr[i] == '0' or cnt >= len(word):
                return False
            
            number = 0
            while i < len(abbr) and ord('0') <= ord(abbr[i]) <= ord('9'):
                number = number * 10 + (ord(abbr[i]) - ord('0'))
                i += 1
            
            if number > 0:
                cnt += number
            else:
                if abbr[i] != word[cnt]:
                    return False
                cnt += 1
                i += 1
        return cnt == len(word)
        