class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)
        N = len(nums)
        ans = []
        for i in range(N):
            if i>0 and nums[i] == nums[i - 1]:
                continue
            l,r = i + 1, N - 1

            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s == 0:
                    triplet = [nums[l], nums[i], nums[r]]
                    ans.append(triplet)
                    while l < r and nums[l] == nums[l + 1] :
                        l += 1
                    while l<r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return ans