words = ["gin", "zen", "gig", "msg"]

class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        uniqueMorseCode = set()
        for word in words:
            code = ''
            for eachLetter in word:
                eachCode = morse[alphabet.index(eachLetter)]
                code = code + eachCode
            uniqueMorseCode.add(code)
        return len(uniqueMorseCode)