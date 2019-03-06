nums = [2,2,1,1,1,2,2]
nums=[3,2,3]
count = {}
for num in nums:
    if num in count.keys():
        count[num] += 1
    else:
        count[num] = 1
    if count[num] > len(nums)/2:
        print(num)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
            if count[num] > len(nums) / 2:
                return num