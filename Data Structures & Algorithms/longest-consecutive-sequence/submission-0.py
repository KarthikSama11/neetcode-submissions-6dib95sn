class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for ele in s:
            if ele - 1 in s:
                continue
            count = 1
            while ele + 1 in s:
                count += 1
                ele += 1
            res = max(res, count)
        return res