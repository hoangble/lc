# class Node():
#     def __init__(self):
#         self.is_end = ""
#         self.edges = {}

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie_head = Node()
#         for word in words:
#             tmp = trie_head
#             for c in word:
#                 if c not in tmp.edges:
#                     child_node = Node()
#                     tmp.edges[c] = child_node
#                     tmp = child_node
#                 else:
#                     tmp = tmp.edges[c]
#             tmp.is_end = word

#         m, n = len(board), len(board[0])
#         self.visited = []
#         for _ in range(m):
#             self.visited.append([False]*n)

#         ans = set()
#         self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         for i in range(m):
#             for j in range(n):
#                 curr_char = board[i][j]
#                 if curr_char in trie_head.edges:
#                     self.backtrack(board, i, j, trie_head.edges[curr_char], m, n, ans)
#         return ans

#     def backtrack(self, board, x, y, node, m, n, ans):
#         self.visited[x][y] = True

#         if len(node.is_end) != 0:

#             # print(node.is_end)
#             ans.add(node.is_end)
#             node.is_end = ""

#         for direction in self.directions:
#             new_x = x + direction[0]
#             new_y = y + direction[1]

#             if self.in_bound(new_x, new_y, m, n):
#                 if not self.visited[new_x][new_y]:
#                     self.visited[new_x][new_y] = True
#                     if board[new_x][new_y] in node.edges:
#                         curr_char = board[new_x][new_y]
#                         self.backtrack(board, new_x, new_y, node.edges[curr_char], m, n, ans)
#                         # del node.edges[curr_char]
#                     self.visited[new_x][new_y] = False
#         self.visited[x][y] = False

#         if board[x][y] in node.edges:
#             print(node.edges[board[x][y]])
#             node.edges.pop(board[x][y])

#     def in_bound(self, new_x, new_y, m, n):
#         return 0 <= new_x < m and 0 <= new_y < n


#     # def visit_trie(self, node):
#     #     if len(node.is_end) != 0:
#     #         # print(node.is_end)
#     #         return

#     #     for edge in node.edges:
#     #         self.visit_trie(node.edges[edge])


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "$"

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = "#"

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords
