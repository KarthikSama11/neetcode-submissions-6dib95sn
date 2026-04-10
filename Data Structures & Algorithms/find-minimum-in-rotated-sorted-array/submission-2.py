class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if nums[l] < nums[mid]: we are in left sorted arr
        # if num[mid] < nums[r] : we are in right sorted arr
        N = len(nums)
        l,r = 0, N - 1
        res = 1e9 + 7
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < nums[r]:
                res = min(nums[mid],res)
                r = mid - 1
            else:
                res = min(res, nums[r])
                l = mid + 1
            
        return res