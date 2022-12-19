# https://leetcode.com/problems/word-ladder/description/
# 127. Word Ladder


from collections import deque
from copy import deepcopy
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList = set(wordList)
        queue = deque()
        queue.append((beginWord, 0))
        visited = set()
        visited.add(beginWord)
        
        # too slow
        # while queue:
        #     curr_word, n_step = queue.popleft() 

        #     if curr_word == endWord: return n_step + 1

        #     for dict_word in wordList:
        #         if self.cal_hamming_dist(dict_word, curr_word) and dict_word not in visited:
        #             visited.add(dict_word)
        #             queue.append((dict_word, n_step + 1))
        # return 0

        while queue:
            curr_word, n_step = queue.popleft() 

            if curr_word == endWord: return n_step + 1

            letters = [*curr_word]
            for i in range(len(letters)):
                for c in range(97, 123):
                    letters_copy = deepcopy(letters)
                    letters_copy[i] = chr(c)
                    new_word = "".join(letters_copy)
                    if new_word in wordList and new_word not in visited:
                        queue.append((new_word, n_step + 1))
                    visited.add(new_word)
        return 0
