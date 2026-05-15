class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_seen = {}
        for i, val in enumerate(nums):
            find = target - val
            if find in num_seen:
                return [num_seen[find], i]
            else:
                num_seen[val]=i
        return []