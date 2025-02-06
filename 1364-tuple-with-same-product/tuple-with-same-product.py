class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        f=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                f[nums[i]*nums[j]]+=1
        
        total=0
        for key in f.keys():
            total+=f[key]*(f[key]-1) * 4        
        return total
