class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        cur_sum = 0

        for i in reversed(range(len(nums))) :
            cur_sum += nums[i]
            remaining = total - cur_sum

            if remaining > nums[i]:
                return remaining + nums[i]
        return -1
