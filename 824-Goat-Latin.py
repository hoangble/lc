class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        vowels = set((
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U'
        ))
        ans = []

        for i, w in enumerate(words, 1):
            chrs = [*w] # convert to list as list manipulation is cheaper
            new_w = chrs
            if chrs[0] not in vowels:
                new_w = new_w[1:]
                new_w.append(chrs[0])
            
            new_w.append('m')
            new_w.append('a')
            new_w += ['a'] * i
            ans.append(''.join(new_w))
        return ' '.join(ans)
        