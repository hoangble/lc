class Solution:
    def frequencySort(self, s: str) -> str:
        max_freq = -1
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
            if counter[c] > max_freq:
                max_freq = counter[c]
        # print(max_freq)
        buckets = [[] for _ in range(max_freq + 1)]

        for k, v in counter.items():
            # print(k, v)
            buckets[v].append(k)

        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(buckets[i]) > 0:
                for c in buckets[i]:
                    ans += [c] * i
        return ''.join(ans)