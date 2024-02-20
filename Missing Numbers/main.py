class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        c = Counter(nums)
        N = len(nums)

        for i in range(N+1):
            if i not in c:
                return i
         '''

        N = len(nums)
        SumExp = N*(N+1)//2
        SumAct = sum(nums)
        return SumExp - SumAct
