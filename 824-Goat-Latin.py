class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        vowels = set((
            'a', 'e', 'i', 'o', 'u'
        ))
        ans = []

        for i, w in enumerate(words, 1):
            chrs = [*w]
            # print(chrs)
            new_w = chrs
            if chrs[0].lower() not in vowels:
                new_w = chrs[1:]
                # print(chrs[1:])
                new_w.append(chrs[0])
                # print(new_w)
            
            new_w += ['m', 'a']
            new_w += ['a'] * i
            ans.append(''.join(new_w))
        return ' '.join(ans)
        