nums = [2,2,1]
nums = [4,1,2,1,2]


ans = []
count = {}
for item in nums:
    if item in count.keys():
        count[item] += 1
    else:
        count[item] = 1

for key in count:
    if count[key] == 1:
        ans.append(key)

count[key] == 1

print(ans)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for item in nums:
            if item in count.keys():
                count[item] += 1
            else:
                count[item] = 1

        for key in count:
            if count[key] == 1:
                return key