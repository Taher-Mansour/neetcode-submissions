class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        print(d)
                
        for i in d:
            if(i==target/2 and len(d[i])>1):
                return [d[i][0],d[i][1]]
            p=target-i
            if(p in d):
                if(d[i][0]!=d[p][0]):
                    return [d[i][0],d[p][0]]
        return []