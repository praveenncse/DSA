class NumArray:

    def __init__(self, nums: List[int]):
        self.res=[]
        total=0
        for n in nums:
            total+=n
            self.res.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        preright=self.res[right]
        preleft=self.res[left-1] if left>0 else 0
        return (preright-preleft)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)