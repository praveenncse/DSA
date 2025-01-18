class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        character={'a':0,'b':0,'c':0}
        res=0
        l=0

        for r in range(len(s)):
            character[s[r]]+=1
            while character['a']>0 and character['b']>0 and character['c']>0:
                res+=len(s)-r
                character[s[l]]-=1
                l+=1
            
        return res