class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * (N)

        prefix = 1
        for i in range(N):
            res[i]= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(N-1 , -1,-1): #reverse order
            res[i] *= postfix
            postfix *= nums[i]
        return res
