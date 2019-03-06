nums = [1,2,3,1]
nums = [1,2,3,4]



check = {}
result = False
for num in nums:
    if num in check.keys():
        check[num] += 1
        result = True
    else:
        check[num] = 1
print(result)



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        result = False
        for num in nums:
            if num in check.keys():
                check[num] += 1
                result = True
            else:
                check[num] = 1
        return result
