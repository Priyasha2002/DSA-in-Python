class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        for word in strs:
            key = tuple(sorted(word))  # sort the words in string ("a , e , t" , "a , n , t")

            d[key] = d.get(key , []) + [word] 
        return d.values()
        
