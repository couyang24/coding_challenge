nums1 = [4,1,2]
nums2 = [1,3,4,2]


nums1 = [2,4]
nums2 = [1,2,3,4]

ans = []
for index, item in enumerate(nums1):
    for index2, item2 in enumerate(nums2):
        if item2 == item:
            for item3 in nums2[index2:]:
                if item3 > item:
                    ans.append(item3)
                    break
    if len(ans) == index:
        ans.append(-1)
print(ans)


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for index, item in enumerate(nums1):
            for index2, item2 in enumerate(nums2):
                if item2 == item:
                    for item3 in nums2[index2:]:
                        if item3 > item:
                            ans.append(item3)
                            break
            if len(ans) == index:
                ans.append(-1)
        return ans