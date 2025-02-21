class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        for path in paths:
            p, *files = path.split()
            for f in files:
                name, content = f.split('(')
                g[content].append(p+'/'+name)
        return [name for name in g.values() if len(name) > 1]