class Solution:
    def countDays(self, n: int, a: List[List[int]]) -> int:
        return (E:=0)+sum((max(0,s-E-1),E:=max(e,E))[0] for s,e in sorted(a)+[[n+1]*2])