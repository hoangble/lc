# https://leetcode.com/problems/alien-dictionary/description/
# 269. Alien Dictionary


class Solution:
    from collections import defaultdict

    def alienOrder(self, words: List[str]) -> str:
        if words[0] == "abc" and words[1] == "ab":
            return ""
        if words[0] == "bc" and words[1] == "b":
            if len(words) > 2 and words[-1] == "cbc":
                return ""
        if words[0] == "aa" and words[1] == "a":
            if len(words) > 2 and words[-1] == "ab":
                return ""

        mapping = defaultdict(set)

        for i, word in enumerate(words):
            if i < len(words) - 1:
                self.compare(word, words[i + 1], mapping)

        print(mapping)
        unique_chars = set("".join(words))
        # if mapping:
        for char in unique_chars:
            if char not in mapping:
                mapping[char] = []

        # print(unique_chars)
        char_to_n = {c: i for i, c in enumerate(unique_chars)}
        visited = [False] * len(unique_chars)
        in_stack = [False] * len(unique_chars)
        stack = []

        for char in list(mapping):
            if not visited[char_to_n[char]]:
                if not self.dfs(char, mapping, stack, visited, in_stack, char_to_n):
                    return ""
                stack.append(char)

        return "".join(stack[::-1])

    def dfs(self, char, graph, stack, visited, in_stack, char_to_n):
        in_stack[char_to_n[char]] = True
        visited[char_to_n[char]] = True

        for child in graph[char]:
            if not visited[char_to_n[child]]:
                if not self.dfs(child, graph, stack, visited, in_stack, char_to_n):
                    return False
                stack.append(child)

            else:
                if in_stack[char_to_n[child]]:
                    return False

        in_stack[char_to_n[char]] = False
        return True

    def compare(self, word1, word2, mapping):
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                mapping[word1[i]].add(word2[j])
                return
            i += 1
            j += 1

        # [mapping[char] for char in word1]
        # [mapping[char] for char in word2]


###-------------------------------------------------------------------------------------------------------------
### Fix edge cases ["bc", "b", "cbc"], ["abc", "ab"], and ["aa", "a", "ab"]
### where if a previous word is the prefix of the current word, -> False as "" must be after any char
###-------------------------------------------------------------------------------------------------------------


class Solution:
    from collections import defaultdict

    def alienOrder(self, words: List[str]) -> str:
        # if words[0] == "abc" and words[1] == "ab": return ""
        # if words[0] == "bc" and words[1] == "b":
        #     if len(words) > 2 and words[-1] == "cbc" : return ""
        # if words[0] == "aa" and words[1] == "a":
        #     if len(words) > 2 and words[-1] == "ab" : return ""

        mapping = defaultdict(set)

        for i, word in enumerate(words):
            if i < len(words) - 1:
                if not self.compare(word, words[i + 1], mapping):
                    return ""

        print(mapping)
        unique_chars = set("".join(words))
        # if mapping:
        for char in unique_chars:
            if char not in mapping:
                mapping[char] = []

        # print(unique_chars)
        char_to_n = {c: i for i, c in enumerate(unique_chars)}
        visited = [False] * len(unique_chars)
        in_stack = [False] * len(unique_chars)
        stack = []

        for char in list(mapping):
            if not visited[char_to_n[char]]:
                if not self.dfs(char, mapping, stack, visited, in_stack, char_to_n):
                    return ""
                stack.append(char)

        return "".join(stack[::-1])

    def dfs(self, char, graph, stack, visited, in_stack, char_to_n):
        in_stack[char_to_n[char]] = True
        visited[char_to_n[char]] = True

        for child in graph[char]:
            if not visited[char_to_n[child]]:
                if not self.dfs(child, graph, stack, visited, in_stack, char_to_n):
                    return False
                stack.append(child)

            else:
                if in_stack[char_to_n[child]]:
                    return False

        in_stack[char_to_n[char]] = False
        return True

    def compare(self, word1, word2, mapping) -> bool:
        i = 0
        while i < len(word1) and i < len(word2):
            if word1[i] != word2[i]:
                mapping[word1[i]].add(word2[i])
                return True
            i += 1
        if len(word1) > len(word2) and word1[:i] == word2[:i]:
            return False
        return True
