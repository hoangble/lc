class AutocompleteSystem:
    from collections import deque

    def __init__(self, sentences: List[str], times: List[int]):
        self.head = Node()

        for sen, t in zip(sentences, times):
            tmp = self.head
            for c in sen:
                if not c in tmp.edges:
                    node = Node()
                    tmp.edges[c] = node

                tmp.edges[c].word_cnt[sen] += t
                tmp = tmp.edges[c]
        print_trie(self.head)
        self.search_ptr = self.head
        self.prev_input = ""

    def input(self, c: str) -> List[str]:
        print(c)
        ans = {}
        if c != "#":
            self.prev_input += c
            self.dfs(c, ans)
            sorted_ans = {
                k: v for k, v in sorted(ans.items(), key=lambda x: (-x[1], x[0]))
            }
            to_return = []
            i = 0
            for k, v in sorted_ans.items():
                if i < 3:
                    to_return.append(k)
                    i += 1
            return to_return
        else:
            tmp = self.head
            for c in self.prev_input:
                if not c in tmp.edges:
                    node = Node()
                    tmp.edges[c] = node

                # for sen, cnt in tmp.edges[c].word_cnt.items():
                tmp.edges[c].word_cnt[self.prev_input] += 1
                tmp = tmp.edges[c]

            self.search_ptr = self.head
            self.prev_input = ""

            return []

    def dfs(self, c, ans) -> dict:
        if c in self.search_ptr.edges:
            for sen, cnt in self.search_ptr.edges[c].word_cnt.items():
                ans[sen] = cnt
            self.search_ptr = self.search_ptr.edges[c]
        return ans


class Node:
    from collections import defaultdict

    def __init__(self):
        self.word_cnt = defaultdict(
            int
        )  # {possible word with curr prefix: n times appeared}
        self.edges = {}


def print_trie(head):
    q = [head]
    while q:
        curr_q = []
        next_q = []
        for q_ in q:
            curr_q.append(q_.word_cnt)
            # print(q_.edges)
            for _, edge in q_.edges.items():
                # print(edge)
                next_q.append(edge)
        q = next_q
        print(curr_q)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
