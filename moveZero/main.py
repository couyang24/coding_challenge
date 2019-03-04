nums = [0,1,0,3,12]
count = 0
ans = []
for num in nums:
    if num != 0:
        ans.append(num)
    else:
        count += 1
for zero in range(count):
    ans.append(0)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        ans = []
        for num in nums:
            if num != 0:
                ans.append(num)
            else:
                count += 1
        for zero in range(count):
            ans.append(0)
        return ans



for index in range(len(nums)):
    if nums[index] == 0:
        nums.pop(nums.index(0))
        nums.append(0)