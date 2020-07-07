class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans =0
        r=len(grid)
        if r==0:
            return ans
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    ans+=4
                    if i-1>=0 and grid[i-1][j]==1:
                        ans-=1
                    if j-1>=0 and grid[i][j-1]==1:
                        ans-=1
                    if i+1<r and grid[i+1][j]==1:
                        ans-=1
                    if j+1<c and grid[i][j+1]==1:
                        ans-=1
        return ans
        
