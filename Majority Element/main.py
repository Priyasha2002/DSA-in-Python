class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count= 0
        for n in nums :
         if count ==0:
            res = n
         count += (1 if n == res else -1)
        return res 
        
#Another Solution 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        output = 0
        max_count = 0

        for k , v in counter.items():
            if v > max_count :
                max_count += v
                output = k
        return output 
