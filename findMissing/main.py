nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
max(nums)
min(nums)




if nums == []:
    print([])


ans = []
for num in range(min(nums), len(nums)+1):
    if num not in nums:
        ans.append(num)

print(ans)














class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in range(min(nums), max(nums) + 1):
            if num not in nums:
                ans.append(num)
        return ans