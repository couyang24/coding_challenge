S = "a1b2"
#letters = ''
#letters = [[c.lower(), c.upper()] for c in S if c.isalpha()]


ans = ['']
for item in S:
    if item.isalpha():
        ans = [i+j for i in ans for j in [item.upper(), item.lower()]]
    else:
        ans = [i+j for i in ans for j in item]
print(ans)

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        for item in S:
            if item.isalpha():
                ans = [i + j for i in ans for j in [item.upper(), item.lower()]]
            else:
                ans = [i + j for i in ans for j in item]
        return ans