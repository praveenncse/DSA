class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a = list(str(n))

        def back(arr, el):

            if not arr:
                if el[0] != "0":
                    # print(el)
                    if int(el) & int(el) - 1 == 0:
                        return True
                
                return False
            
            ans = False
            for i in range(len(arr)):
                ans = back(arr[:i] + arr[i + 1:], el + arr[i])
                if ans: return True

            return ans
        
        return (back(a, ""))