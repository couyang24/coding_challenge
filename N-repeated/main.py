
A = [1,2,3,3]



class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        counter = {}
        for input in A:
            if input in counter.keys():
                print(input)
            else:
                counter[input] = 1

