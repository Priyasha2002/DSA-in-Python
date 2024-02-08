class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set ()
        # sliding window needs two pointer and right . ledt is initially 0 but righ pointer will iterate through all characters
        l = 0
        res = 0

        for r in range (len(s)) :
            while s[r] in charSet : # if duplicates
                charSet.remove(s[l]) # remove the ledt element
                l += 1               # go to the next elemrnt from left to right
            charSet.add(s[r])        # if no duplicates , add the right most element to the substring
            res = max (res , r-l+1)  # res = max of (0 , r-l+1) : r-l+1 gives the length of current substring
        return res 
