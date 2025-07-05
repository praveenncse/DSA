class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt=-1
        freq=Counter(arr)

        for num,count in freq.items():
            if num==count:
                cnt=max(cnt,num)
        return cnt