S = "loveleetcodedd"
C = 'e'

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for index, letter in enumerate(S):
            if letter == C: prev = index
            ans.append(index - prev)

            next = float('inf')
            for index2, letter2 in enumerate(S[index:]):
                if letter2 == C:
                    next = index2
                    break

            if next < index - prev:
                ans[index] = next

        return ans
