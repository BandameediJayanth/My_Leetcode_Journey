class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefmax = [0] * n
        sufmin = [0] * n
        prefmax[0] = nums[0]
        for i in range(1,n):
            prefmax[i] = max(prefmax[i-1], nums[i])

        sufmin[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            sufmin[i] = min(sufmin[i+1],nums[i])

        ans = float('inf')
        for i in range(n):
            cur = prefmax[i] - sufmin[i]
            if cur <= k:
                ans = min(ans,i)
        if ans!= float('inf'):
            return ans
        else:
            return -1

        