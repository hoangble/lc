class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strings:
            hash_key = self.get_hash(s)
            group[hash_key].append(s)
        return list(group.values())
    
    def get_hash(self, s):
        curr = []
        for a, b in zip(s, s[1:]):
            k = (ord(a) - ord(b)) % 26
            curr.append(k)
        return tuple(curr)