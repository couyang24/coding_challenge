s = "anagram"
t = "nagaram"

checkS = {}
checkT = {}

for letter in s:
    if letter in checkS.keys():
        checkS[letter] += 1
    else:
        checkS[letter] = 1

for letter in t:
    if letter in checkT.keys():
        checkT[letter] += 1
    else:
        checkT[letter] = 1

print(checkT==checkS)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = {}
        checkT = {}

        for letter in s:
            if letter in checkS.keys():
                checkS[letter] += 1
            else:
                checkS[letter] = 1

        for letter in t:
            if letter in checkT.keys():
                checkT[letter] += 1
            else:
                checkT[letter] = 1
        return checkT == checkS