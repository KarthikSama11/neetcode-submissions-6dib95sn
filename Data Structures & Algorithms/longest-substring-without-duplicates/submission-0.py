class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        
        #maintain a set to track all elements in cur window
        #left to right would be cur window
        #when you find a duplicate, until there are all chars, 
        #you start moving the shrinking the window from left
        N = len(s)
        l = 0
        res = 0
        for r in range(N):
            freq[s[r]]+= 1
            while r - l + 1 > len(freq):
                #there aer duplicates
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            print(freq)
            res = max(res, r - l + 1)
        return res
                

        