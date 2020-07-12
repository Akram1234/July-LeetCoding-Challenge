# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        for _ in range(32):
            ans |= ((n>>_)&1)<<(31-_)
        return ans
