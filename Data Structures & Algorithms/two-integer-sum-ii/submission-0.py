class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pt_rg = 0
        pt_lt = len(numbers)-1
        while pt_rg < pt_lt:
            if numbers[pt_rg] + numbers[pt_lt]<target:
                pt_rg +=1
            elif numbers[pt_rg] + numbers[pt_lt]>target:
                pt_lt -=1
            else:
                return [pt_rg+1, pt_lt+1]
        return []