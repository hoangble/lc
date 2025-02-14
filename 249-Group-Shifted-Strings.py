class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # convert everthing to how an a-starting string
        group = defaultdict(list)
        for s in strings:
            hash_key = self.get_hash(s)
            group[hash_key].append(s)
        
        return list(group.values())

    def get_hash(self, s):
        key = []
        for a, b in zip(s, s[1:]):
            curr = (ord(a)-ord(b)) % 26 + ord('a')
            key.append(chr(curr))
        return ''.join(key)
