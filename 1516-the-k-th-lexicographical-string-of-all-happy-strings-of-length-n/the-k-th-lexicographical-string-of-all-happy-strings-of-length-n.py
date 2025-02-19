class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        start_div = (1 << (n - 1))
        if k > start_div * 3:
            return ""
        
        nex = {
            'a': ['b', 'c'],
            'b': ['a', 'c'],
            'c': ['a', 'b']
        }
        k -= 1
        ans = []
        ans.append(chr((k // start_div) + ord('a')))
        k %= start_div
        
        for i in range(n - 2, -1, -1):
            ans.append(nex[ans[-1]][k // (1 << i)])
            k %= (1 << i)
        return "".join(ans)