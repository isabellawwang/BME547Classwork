import json


def input_json(filename):
    in_file = open(filename, 'r')
    new_variable = json.load(in_file)
    in_file.close()
    return new_variable


if __name__ == "__main__":
    filename = "my_booleans.json"
    x = input_json(filename)
    print(x)
    print(type(x))
