class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        # print(waiting)

        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])