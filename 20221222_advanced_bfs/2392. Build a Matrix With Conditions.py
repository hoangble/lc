# https://leetcode.com/problems/build-a-matrix-with-conditions/
# 2392. Build a Matrix With Conditions
from typing import List


class Solution:
    from collections import defaultdict

    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        row_mapping = defaultdict(set)
        self.build_graph(row_mapping, rowConditions)
        for row in range(1, k + 1):
            if row not in row_mapping:
                row_mapping[row] = []
        print("row mapping", row_mapping)

        row_visited = [False] * k
        row_in_stack = [False] * k
        row_stack = []

        for node in list(row_mapping):
            if not row_visited[node - 1]:
                if not self.dfs(
                    node, row_mapping, row_visited, row_in_stack, row_stack
                ):
                    return []
                row_stack.append(node)

        col_mapping = defaultdict(set)
        self.build_graph(col_mapping, colConditions)
        for col in range(1, k + 1):
            if col not in col_mapping:
                col_mapping[col] = []
        print("col mapping", col_mapping)

        col_visited = [False] * k
        col_in_stack = [False] * k
        col_stack = []

        for node in list(col_mapping):
            if not col_visited[node - 1]:
                if not self.dfs(
                    node, col_mapping, col_visited, col_in_stack, col_stack
                ):
                    return []
                col_stack.append(node)

        row_stack = row_stack[::-1]
        col_stack = col_stack[::-1]

        print("row_stack", row_stack)
        print("col_stack", col_stack)

        matrix = []
        for i in range(k):
            matrix.append([0] * k)
        row = 0

        matrix_mapping = defaultdict(list)
        for idx, row_node in enumerate(row_stack):
            matrix_mapping[row_node].append(idx)

        for idx, col_node in enumerate(col_stack):
            matrix_mapping[col_node].append(idx)

        print(matrix_mapping)

        for key, value in matrix_mapping.items():
            print(key, value)
            matrix[value[0]][value[1]] = key
        return matrix

    def build_graph(self, mapping, conditions):
        for condition in conditions:
            mapping[condition[0]].add(condition[1])

    def dfs(self, node, graph, visited, in_stack, stack) -> bool:
        visited[node - 1] = True
        in_stack[node - 1] = True

        for child in graph[node]:
            if not visited[child - 1]:
                if not self.dfs(child, graph, visited, in_stack, stack):
                    return False
                stack.append(child)
            else:
                if in_stack[child - 1]:
                    return False
        in_stack[node - 1] = False
        return True
