class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==0:
            return 0
        s=0
        ans = 0
        for i in range(1, n+1):
            s+=i
            if s<=n:
                ans = i
            else:
                break
        return ans
