class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergeSort(nums:List[int]):
            if len(nums)<=1:
                return nums
            mid = len(nums)//2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left,right)

        def merge(left:List[int],right:List[int]) -> List[int]:
            i,j = 0,0
            result = []
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        nums[:] = mergeSort(nums)
        return
