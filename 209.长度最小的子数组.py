class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n_sum = 0
        min_length = len(nums)+1
        for right,x in enumerate(nums):
            n_sum += x
            while n_sum >= target:
                min_length = min(min_length,right-left+1)
                n_sum -= nums[left]
                left += 1
        return min_length if min_length<=len(nums) else 0
