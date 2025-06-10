class Solution:
    def maxDifference(self, s: str) -> int:
        freq=defaultdict(int)
        for c in s:
            freq[c]+=1

        even_freq=[]
        odd_freq=[]

        for count in freq.values():
            if count%2==0:
                even_freq.append(count)
            else:
                odd_freq.append(count)

        max_odd=max(odd_freq)
        min_even=min(even_freq)

        return max_odd-min_even