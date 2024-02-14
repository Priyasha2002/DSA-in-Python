class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # seperate the positive and the negative numbrs using list comprehension
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]

        #Initialize an empty list to store the result
        res = []

        #Loop over half the length of the original array
        #append the positive and negative nums alternatively into the res

        for i in range(len(nums) //2) :
            res.append(positives[i])
            res.append(negatives[i])
        return res
