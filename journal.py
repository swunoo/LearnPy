# The dictionary is converted to a json string.
import json

# Function that reads a dictionary from a file
def read_from_file (filename):
    try:
        f = open(filename, 'r')
        res = f.read()
    except:
        print('file not found.')
        return {}

    try:
        json_dict = json.loads(res)
    except:
        print('file not in json format.')
        json_dict = {}
    finally:
        f.close()
        return json_dict

# Function that inverts a dictionary
def invert_dictionary (d):
     inverse = dict()
     for l in d:
        for val in d[l]: 
            if val not in inverse:
               inverse[val] = [l]
            else:
               inverse[val].append(l)
     return inverse 

# Function that writes a dictionary to a file
def write_to_file(d, filename):
    json_dict = json.dumps(d)
    f = open(filename, 'w')
    f.write(json_dict)
    f.close()

my_dict = read_from_file('input_file.txt')

inverted_dict = invert_dictionary(my_dict)

write_to_file(inverted_dict, 'output_file.txt')
