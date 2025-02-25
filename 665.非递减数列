# 贪心算法
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        num = 0
        nums = [min(nums)] + nums + [max(nums)]
        n = len(nums)
        for i in range(1,n-1):
            if nums[i]>=nums[i-1] and nums[i]<=nums[i+1]:
                continue
            elif num==0 and nums[i+1]>=nums[i-1]:
                nums[i] = nums[i-1]
                num += 1
            elif num == 0 and nums[i]>=nums[i-1]:
                nums[i+1] = nums[i]
                num+=1
            else:
                return False
        return True
