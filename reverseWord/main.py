s = "Let's take LeetCode contest"

s.split()

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        for eachWord in s.split():
            newWord = ''
            for eachLetter in eachWord[::-1]:
                newWord = newWord + eachLetter
            ans = ans + ' ' + newWord
        return ans.strip()

