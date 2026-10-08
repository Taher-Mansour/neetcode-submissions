class Solution:
    def search(self, nums: List[int], target: int) -> int:
        prm=0
        drn=len(nums)-1
        while(prm<=drn):
            mlu=(prm+drn)//2
            if(nums[mlu]==target):
                return mlu
            elif (target<nums[mlu]):
                drn=mlu-1
            else:
                prm=mlu+1
        return -1
   