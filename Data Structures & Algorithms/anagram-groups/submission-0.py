class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        umap = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for ch in word:
                letterInd = ord(ch) - ord('a')
                freq[letterInd]+= 1
            key = ','.join(map(str,freq))
            umap[key].append(word)
        print(len(umap))
        for key, value in umap.items():
            ans.append(value.copy())
        return ans