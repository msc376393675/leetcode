class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l,r = 0,0
        ans = []
        if len(nums)!=0:
            while r<len(nums)-1:
                if nums[r] + 1 != nums[r+1]:
                    if l == r:
                        ans.append(f'{nums[l]}')
                    else:
                        ans.append(f'{nums[l]}->{nums[r]}')
                    l = r+1
                r += 1    
            if l==r:
                ans.append(f'{nums[l]}')
            else:
                ans.append(f'{nums[l]}->{nums[r]}')
        return ans
        
