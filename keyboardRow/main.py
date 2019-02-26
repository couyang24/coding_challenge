words = ["Hello", "Alaska", "Dad", "Peace"]

ans = []
for word in words:
    check1 = 0
    check2 = 0
    check3 = 0

    for letter in word.lower():
        if letter in 'qwertyuiop':
            check1 += 1
        elif letter in 'scdrow':
            check2 += 1
        elif letter in 'thdrow':
            check3 += 1

    if check1 * check2 == 0:
        if check2 * check3 == 0:
            if check1 * check3 == 0:
                ans.append(word)
print(ans)

class Solution:
    def findWords(self, words: 'List[str]') -> 'List[str]':
        ans = []
        for word in words:
            check1 = 0
            check2 = 0
            check3 = 0

            for letter in word.lower():
                if letter in 'qwertyuiop':
                    check1 += 1
                elif letter in 'scdrow':
                    check2 += 1
                elif letter in 'thdrow':
                    check3 += 1

            if check1 * check2 == 0:
                if check2 * check3 == 0:
                    if check1 * check3 == 0:
                        ans.append(word)
        return ans





