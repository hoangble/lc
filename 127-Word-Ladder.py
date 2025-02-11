class Solution:
    from collections import deque
    from copy import deepcopy

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList = set(wordList)
        all_unique_chars = set()
        for word in wordList:
            for ch in word:
                all_unique_chars.add(ch) 

        q = deque([])
        q.append((beginWord, 0))
        visited = set()
        visited.add(beginWord)

        all_combos_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combos_dict[word[:i] + \*\ + word[i+1:]].append(word)

        while q:
            curr, n_step = q.popleft()

            if curr == endWord:
                return n_step + 1

            letters = [*curr]

            for i in range(len(letters)):
                immediate_combos = ''.join([curr[:i], \*\, curr[i+1:]])
                # copy_letters = deepcopy(letters)
                # for ch in all_unique_chars:
                for new_word in all_combos_dict[immediate_combos]:
                    # copy_letters[i] = ch
                    # new_word = ''.join(copy_letters)
                    if new_word in wordList and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, n_step + 1))
        return 0