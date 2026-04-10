class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreq = [0]*26
        tfreq = [0]*26
        
        for c in s:
            ind = ord(c) - ord('a')
            sfreq[ind] += 1
        for c in t:
            ind = ord(c) - ord('a')
            tfreq[ind] += 1
        
        return sfreq == tfreq
        