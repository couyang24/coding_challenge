nums = [4,3,2,7,8,2,3,1]
nums = [1,1]
nums = [2,2]

max(nums)
min(nums)




if nums == []:
    print([])


ans = []
for num in range(1, len(nums)+1):
    if num not in nums:
        ans.append(num)

print(ans)


def findDisappearedNumbers(nums):
    if nums == []:
        return []
    ans = []
    for num in range(1, len(nums) + 1):
        if num not in nums:
            ans.append(num)
    return ans

findDisappearedNumbers(nums)


class Solution:
    def findDisappearedNumbers(self, nums):
        if nums == []:
            return []
        ans = []
        for num in range(1, len(nums) + 1):
            if num not in nums:
                ans.append(num)
        return ans
