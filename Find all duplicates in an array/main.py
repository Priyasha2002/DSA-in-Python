class Solution:
    def findDuplicates(self, nums):
        duplicates = []
        
        for num in nums:
            # Get the absolute value of the number
            abs_num = abs(num)
            
            # If the number at index abs_num - 1 is negative, it means abs_num has occurred before
            # Hence, it's a duplicate
            if nums[abs_num - 1] < 0:
                duplicates.append(abs_num)
            else:
                # Mark the number at index abs_num - 1 as negative to indicate it has occurred once
                nums[abs_num - 1] *= -1
        
        return duplicates
