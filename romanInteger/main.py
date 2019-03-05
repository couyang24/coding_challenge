s = "III"
s="LVIII"

index = 0

roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
count = 0
for index in range(len(s)):
    if index < len(s)-1 and roman[s[index]] < roman[s[index+1]]:
        count -= roman[s[index]]
    else:
        count += roman[s[index]]

print(count)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        count = 0
        for index in range(len(s)):
            if index < len(s) - 1 and s[index] < s[index + 1]:
                count -= roman[s[index]]
            else:
                count += roman[s[index]]
        return count


