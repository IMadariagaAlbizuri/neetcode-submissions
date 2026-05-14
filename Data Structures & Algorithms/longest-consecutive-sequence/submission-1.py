class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_list = sorted(set(nums))
        prev = 0
        seq = 0
        maxi = 0
        for i in range(len(num_list)):
            if num_list[i]==prev+1:
                seq +=1
            else:
                seq = 1
            prev = num_list[i]
            if seq > maxi:
                maxi = seq
        return maxi
