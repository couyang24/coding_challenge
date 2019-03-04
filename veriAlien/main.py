words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

check = {}
for index, letter in enumerate(order):
    check[letter] = index


len(words)

for index in range(1, len(words)-1):
    words[0][index]