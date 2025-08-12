class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        p = [q**x for q in range(1,round(n**(1/x))+1)]

        @cache
        def f(i,n):
            if i<len(p) and n>=p[i]:
                return (f(i+1,n)+f(i+1,n-p[i]))%(10**9+7)
            return int(n==0)
            
        return f(0,n)