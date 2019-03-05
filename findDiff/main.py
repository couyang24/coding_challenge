s = "abcd"
t = "abcde"



'd' in t


for letter in t:
    if letter not in s:
        print(letter)





class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if letter not in s:
                return letter



count = {}
for letter in t:
    if letter not in s:
        print(letter)
    elif letter in count.keys():
        print(letter)
    else:
        count[letter] = 1

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for letter in t:
            if letter not in s:
                return letter
            elif letter in count.keys():
                return letter
            else:
                count[letter] = 1


countS = {}
countT = {}
for letter in s:
    if letter in countS.keys():
        countS[letter] += 1
    else:
        countS[letter] = 1

for letter in t:
    if letter in countT.keys():
        countT[letter] += 1
    else:
        countT[letter] = 1

for letter in countT.keys():
    if letter not in countS.keys() or countT[letter] != countS[letter]:
        print(letter)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countS = {}
        countT = {}
        for letter in s:
            if letter in countS.keys():
                countS[letter] += 1
            else:
                countS[letter] = 1

        for letter in t:
            if letter in countT.keys():
                countT[letter] += 1
            else:
                countT[letter] = 1

        for letter in countT.keys():
            if letter not in countS.keys() or countT[letter] != countS[letter]:
                return letter