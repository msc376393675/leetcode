import random
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pivot_val = random.choice(nums)
        larger, equal, smaller = [], [], []
        for num in nums:
            if num > pivot_val:
                larger.append(num)
            elif num < pivot_val:
                smaller.append(num)
            else:
                equal.append(num)
        if k <= len(larger):
            return self.findKthLargest(larger, k)
        if k > len(larger) + len(equal):
            return self.findKthLargest(smaller, k - len(larger) - len(equal))
        return pivot_val
