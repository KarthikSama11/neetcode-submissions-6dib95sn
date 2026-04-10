class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefixarr = [nums[0]]*len(nums)
        suffixarr = [nums[N-1]]*len(nums)
        ans = [0]*N
        for i in range(0, N):
            prefix = 1 if i == 0 else prefixarr[i - 1]
            suffix = 1 if i == 0 else suffixarr[N - i]
            prefixarr[i] = prefix * nums[i]
            suffixarr[N - i - 1] = suffix * nums[N - i - 1]
        for i in range(N):
            prefix = 1 if i ==0 else prefixarr[i - 1]
            suffix = 1 if i == N - 1 else suffixarr[i + 1]
            ans[i] = prefix * suffix
        return ans