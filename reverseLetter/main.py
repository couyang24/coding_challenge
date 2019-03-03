S = "ab-cd"

letters = [c for c in S if c.isalpha()]

letters[-1]

#print(letters[::-1][-1])
count = 0
ans = ''
for item in S:
    if item.isalpha():
        count -= 1
        ans += letters[count]
    else:
        ans += item
print(ans)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        count = 0
        ans = ''
        for item in S:
            if item.isalpha():
                count -= 1
                ans += letters[count]
            else:
                ans += item
        return ans