class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        output=[1]*len(nums)
        running = 1
        for i in range(len(nums)):
            left[i]=running
            running *= nums[i]
        running = 1
        for j in range(len(nums)-1, -1, -1):
            right[j]=running
            running *= nums[j]
        for m in range(len(left)):
            output[m]=left[m]*right[m]
        return output
