input_ints = [4, 1, 1, 1, 1, 2, 2, 2, 3, 3]

def findTopTwo(input_ints):
    result = {}
    for input_int in input_ints:
        if input_int in result.keys():
            result[input_int] += 1
        else:
            result[input_int] = 1
    fst_freq = sorted(result.values())[-1]
    snd_freq = sorted(result.values())[-2]

    for key, value in result.items():
        if value == fst_freq:
            print(key)
        elif value == snd_freq:
            print(key)


findTopTwo(input_ints)