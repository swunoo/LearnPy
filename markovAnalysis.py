def make_dict_uno(file):

    word_dict = dict()

    for line in file:
        line_list = line.strip().split(' ')

        for i in range(0,len(line_list) - 1):
            if(line_list[i] in word_dict):
                if(line_list[i+1] in word_dict[line_list[i]]):
                    word_dict[line_list[i]][line_list[i+1]] += 1
                else:
                    word_dict[line_list[i]][line_list[i+1]] = 1
            else:
                word_dict[line_list[i]] = {line_list[i+1] : 1}

    return word_dict

def make_dict_dos(file):
    word_dict = dict()

    for line in file:
        line_list = line.strip().split(' ')

        for i in range(0,len(line_list) - 2):
            if((line_list[i], line_list[i+1]) in word_dict):
                if(line_list[i+2] in word_dict[(line_list[i], line_list[i+1])]):
                    word_dict[(line_list[i], line_list[i+1])][line_list[i+2]] += 1
                else:
                    word_dict[(line_list[i], line_list[i+1])][line_list[i+2]] = 1
            else:
                word_dict[(line_list[i], line_list[i+1])] = {line_list[i+2] : 1}

    return word_dict

def probable_suffix(prefix, word_dict):
    if(prefix in word_dict):
        return max_prob(prefix, word_dict)
    else:
        return "Not found."

def max_prob(prefix, word_dict):
    maximum = 0
    max_word = ''
    for ele in word_dict[prefix]:
        if(word_dict[prefix][ele] > maximum):
            maximum = word_dict[prefix][ele]
            max_word = ele
    return max_word

m_file = open('markov.txt')
# m_dict = make_dict_uno(m_file)
m_dict = make_dict_dos(m_file)
print(m_dict)

while(False):
    user_input = input("Prefix: ")
    if(user_input == 'exit'):
        break
    print(probable_suffix(user_input, m_dict))
