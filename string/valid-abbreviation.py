class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_i = 0
        i = 0

        while i < len(abbr):
            if word_i >= len(word) or abbr[i] == "0":
                return False

            num = 0
            while i < len(abbr) and "0" <= abbr[i] <= "9":
                num = num * 10 + (ord(abbr[i]) - ord("0"))
                i += 1

            if num > 0:
                word_i += num
            else:
                if word[word_i] != abbr[i]:
                    return False
                word_i += 1
                i += 1

        return word_i == len(word)


word = "internationalization"
abbr = "i12iz4n"
Solution().validWordAbbreviation(word, abbr)
