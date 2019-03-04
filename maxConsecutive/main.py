nums = [1,1,0,1,1,1]
count = 0
maxCount = 0


for index in range(len(nums)):
    if nums[index] == 0:
        count = 0
    else:
        count += 1
        maxCount = max(maxCount, count)
print(maxCount)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                count = 0
            else:
                count += 1
                maxCount = max(maxCount, count)
        return maxCount