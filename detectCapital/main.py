word = "Dsdfs"

if len(word) > 1:
    if word == word.upper() or word[1:] == word[1:].lower():
        print(True)
    else:
        print(False)
else:
    print(True)



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) > 1:
            if word == word.upper() or word[1:] == word[1:].lower():
                return True
            else:
                return False
        else:
            return True