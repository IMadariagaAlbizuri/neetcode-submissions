class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]
    


          
        