known = {'a': 1}
a = 6

def k ():
    known['a'] = 5
    a = 8
    print(known, a)

# k()
# print(known, a)

def sumall(*args):
    res = 0
    for arg in args:
        res += arg
    return res

# print(sumall(1,2,3,4,5))

def build_freq_dict (file_to_read, file_to_write):

    frequencies = dict()

    f = open (file_to_read, 'r')
    for line in f:
        for letter in line.strip():
            if(letter in frequencies):
                frequencies[letter] += 1
            else:
                frequencies[letter] = 1
    f.close()
    
    f = open('frequencies.txt', 'w')
    for key,value in frequencies.items():
        f.write(key + ',' + str(value) + '\n')
    f.close()

def read_freq_dict(file):
    frequencies = dict()
    f = open(file, 'r')
    for line in f:
        key,value = line.strip().split(',')
        frequencies[key] = value

    f.close()
    print(frequencies)

# read_freq_dict('frequencies.txt')

print((1,3,2) is (1,2,3))








