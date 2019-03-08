# reverse_vowels
#
# input: list of characters
# output: list of characters
#
# input: ['g','r','e','a','t']
# output: ['g','r','a','e','t']
#
#
#          i                           j
# input: ['a','l','l','i','g','a','t','o','r']
# output: ['o','l','l','a','g','i','t','a','r']
#

# create empty list
# forward check if vowel

# if vowels
# once find vowel & create the index for the vowel
# backward and find the vowel with the same index
# append list with the new vowel

# if not vowels
# append list with the non-vowel

# return the list


#       i                               j
lst = ['a', 'l', 'l', 'i', 'g', 'a', 't', 'o', 'r']
lst = ['a', 'e', 'o']


def reverse_vowels(lst):
    i = 0
    j = len(lst) - 1
    vowels = ['a', 'e', 'i', 'o', 'u']
    while i < j:
        if lst[i] not in vowels:
            i += 1
        if lst[j] not in vowels:
            j -= 1
        if lst[i] in vowels and lst[j] in vowels:
            a = lst[i]
            b = lst[j]
            lst[j] = a
            lst[i] = b
            i += 1
            j -= 1
    return lst

# print(reverse_vowels(lst))


# for findex in range(len(lst)):
#     if lst[findex] not in vowels:
#         ans.append(lst[findex])
#     else:
#         fcount += 1
#         for bindex in range(len(lst)):













