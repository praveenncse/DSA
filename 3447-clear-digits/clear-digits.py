class Solution:
    def clearDigits(self, s: str) -> str:
        cnt=0
        res=[]

        for i in reversed(range(len(s))):
            if s[i].isdigit():
                cnt+=1
            elif cnt:
                cnt-=1
            else:
                res.append(s[i])
        return "".join(res[::-1])