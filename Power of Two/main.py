class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        check = 1
        i=1

        while check <= n:
            if check==n:
                return True
            check = 2**i
            i +=1
        return False
