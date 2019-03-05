A = ["bella","label","roller"]


ans = []
for letter in A[0]:
    check = True
    for word in A:
        if letter not in word:
            check = False
    if check == True:
        ans.append(letter)

print(ans)

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        for letter in A[0]:
            check = True
            for word in A:
                if letter not in word:
                    check = False
                else:
                    word
            if check == True:
                ans.append(letter)
        return ans


'cook'['cook'.find('o')]

A.find(word)