class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n , cnt = len(nums) , 0

        freq = defaultdict(int)
        l = 0
        for r,v in enumerate(nums):
            freq[v] += 1
            while freq[v] > k:
                freq[nums[l]] -= 1
                l+=1
            cnt = max(cnt, r - l + 1)

        return cnt
        