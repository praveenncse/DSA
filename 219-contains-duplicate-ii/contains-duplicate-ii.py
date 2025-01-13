class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Bruteforce

        '''for l in range(0,len(nums)):
            for r in range(l+1,min(len(nums),l+k+1)):
                if nums[l]==nums[r]:
                    return True
        return False'''

        # sliding window with fixed size
        l=0
        window=set()
        for r in range(len(nums)):
            if r-l>k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False