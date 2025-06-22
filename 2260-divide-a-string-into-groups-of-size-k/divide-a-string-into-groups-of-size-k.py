class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        curr=0
        n=len(s)

        while curr<n:
            res.append(s[curr:curr+k])
            curr+=k
        res[-1] += fill * (k - len(res[-1]))
        return res