class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_i = 0
        i = 0
        while i < len(abbr):
            if abbr[i] == '0' or word_i >= len(word):
                return False

            num = 0
            while i < len(abbr) and '0' <= abbr[i] <= '9':
                num = num * 10 + (ord(abbr[i]) - ord('0'))
                i += 1

            if num > 0:
                word_i += num
            else:
                if abbr[i] != word[word_i]:
                    return False
                i += 1
                word_i += 1

        return word_i == len(word)

