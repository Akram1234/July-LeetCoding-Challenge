# Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def util(a,b):
            if b==0:
                return 1
            p = util(a,b//2)
            if b%2==0:
                return p*p
            else:
                return a*p*p
        s = -1 if n<0 else 1
        return 1/util(x,abs(n)) if n<0 else util(x,n)
