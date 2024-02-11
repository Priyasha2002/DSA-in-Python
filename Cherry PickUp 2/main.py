class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        num_col, num_rows = len(grid[0]), len(grid)
        
        @lru_cache(None)
        def helper(row, col1, col2):
            #count num of cherries
            cherries = grid[row][col1]
            if col1 != col2:
                cherries += grid[row][col2]
            
            if row == num_rows - 1:
                return cherries
            
            temp = 0
            #all (3 * 3) 9 possibilities 
            for m1 in (col1 - 1, col1 + 1, col1):
                for m2 in (col2 - 1, col2 + 1, col2):
                    if m1 >= 0 and m2 >= 0 and m1 < num_col and m2 < num_col:
                        # we are at a valid point (not outside grid)
                        temp = max(temp, helper(row + 1, m1, m2))
            
            return temp + cherries
        
        return helper(0,0, num_col - 1)
