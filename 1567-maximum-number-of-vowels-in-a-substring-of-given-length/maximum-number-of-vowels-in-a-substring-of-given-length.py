class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        maxcount=0
        cur_count=0

        for i in range(k):
            if s[i] in vowels:
                cur_count+=1
        maxcount=cur_count


        for i in range(k,len(s)):
            if s[i] in vowels:
                cur_count+=1
            if s[i-k] in vowels:
                cur_count-=1
            maxcount=max(cur_count,maxcount)
        return maxcount