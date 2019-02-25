A = [4,2,5,7]


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = []
        even = []
        odd = []
        for item in A:
            if item % 2 == 0:
                even.append(item)
            else:
                odd.append(item)
        while even and odd:
            ans.append(even.pop())
            ans.append(odd.pop())
        return ans