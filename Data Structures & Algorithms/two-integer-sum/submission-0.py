class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        umap = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in umap:
                return [umap[target - num], i]
            umap[num] = i
        return 