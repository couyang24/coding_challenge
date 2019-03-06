A = 'abcde'
B = 'cdeab'

A = 'abcde'
B = 'abced'

if A == "":
    return True

check = False
newA = A
for letter in A:
    if newA == B:
        check = True
    newA = newA[1:]+letter
print(check)



class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        check = False
        newA = A
        for letter in A:
            if newA == B:
                check = True
            newA = newA[1:] + letter
        if A == "" and B == "":
            check = True
        return check
