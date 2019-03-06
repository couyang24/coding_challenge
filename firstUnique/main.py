s = "leetcode"
s = "loveleetcode"



check = False
for index1 in range(len(s)):
    count = 0
    for index2 in range(len(s)):
        if s[index1] == s[index2]:
            count += 1
    if count == 1:
        print(index1)
        check = True
        break
if check == False:
    print(-1)


class Solution:
    def firstUniqChar(self, s: str) -> int:
        check = False
        for index1 in range(len(s)):
            count = 0
            for index2 in range(len(s)):
                if s[index1] == s[index2]:
                    count += 1
            if count == 1:
                return index1
                check = True
                break
        if check == False:
            return -1