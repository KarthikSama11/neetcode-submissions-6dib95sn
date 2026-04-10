class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        ans = []
        for num in nums:
            count[num] += 1
        for num, key in count.items():
            freq[key].append(num)
        print(freq)
        for i in range(len(freq)-1, -1,-1):
            for num in freq[i]:
                if len(ans) == k:
                    return ans
                ans.append(num)
        return ans

        