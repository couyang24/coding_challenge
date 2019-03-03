S = "I speak Goat Latin"
newS = S.split()
ans=[]
for index, word in enumerate(newS):
    if word[0].lower() in ['a','e','i','o','u']:
        ans.append(word+'ma'+'a'*(index+1))
    else:
        ans.append(word[1:]+word[0]+'ma'+'a'*(index+1))
print(' '.join(ans))

class Solution:
    def toGoatLatin(self, S: str) -> str:
        newS = S.split()
        ans = []
        for index, word in enumerate(newS):
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                ans.append(word + 'ma' + 'a' * (index + 1))
            else:
                ans.append(word[1:] + word[0] + 'ma' + 'a' * (index + 1))
        return ' '.join(ans)
