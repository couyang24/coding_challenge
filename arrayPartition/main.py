nums = [1,4,3,2,7,7,8,9,40,1,3,4,7,7]
sorted(nums)
len(nums)




ans = []
for each in range(int(len(nums)/2)):
    ans.append(sorted(nums)[each*2])
print(sum(ans))


sum(sorted(nums)[::2])


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = []
        for each in range(int(len(nums)/2)):
            ans.append(sorted(nums)[each * 2])
        return sum(ans)