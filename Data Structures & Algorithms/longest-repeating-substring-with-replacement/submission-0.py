class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        N = len(s)
        l = 0
        freq = [0]*26
        res = 0
        def maxinarr(arr: list) -> int:
            ans = 0
            for num in arr:
                ans = max(num, ans)
            return ans
        for r, ch in enumerate(s):
            rind = ord(ch) - ord('A')
            freq[rind] += 1
            while r - l + 1 - maxinarr(freq) > k:
                lind = ord(s[l]) - ord('A')
                freq[lind] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res