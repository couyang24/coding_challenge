nums1 = [1,2,2,1]
nums2 = [2,2]


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


ans = []
for num in nums1:
    if num in nums2:
        ans.append(num)

print(list(set(ans)))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            if num in nums2:
                ans.append(num)
        return list(set(ans))