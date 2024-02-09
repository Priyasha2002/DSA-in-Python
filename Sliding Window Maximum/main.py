import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        

        while r < len(nums) : # while r pointer is in bound
            while q and nums[q[-1]] < nums[r] : # remove elements which are smaller than the value u eant to insert
                q.pop()
            q.append(r)

            if l > q[0] : # if l pointer is out of bound
                q.popleft()
            if (r-l+1) == k :
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output
