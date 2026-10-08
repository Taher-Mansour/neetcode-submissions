class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        D={}
        for i in range(len(nums)):
            if nums[i] not in D:
                D[nums[i]]=1
            else:
                D[nums[i]]+=1
        for i in D:
            if(D[i]>1):
                return True
        return False