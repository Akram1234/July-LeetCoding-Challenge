class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        
        for _ in range(32):
            i = 1<<_
            ans += ((x&i)^(y&i))>>_
            # print(i, ans)

        return ans        
