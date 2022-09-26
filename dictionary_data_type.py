def create_dictionary():
    new_dictionary = {"day": "between sunrise and sunset",
                      "food": "something to eat",
                      "night": "when the moon is out"}
    return new_dictionary


def get_from_dictionary(in_dictionary):
    x = in_dictionary["day"]
    # If key doesn't exist, KeyError
    print(x)
    y = in_dictionary.get("dinner")
    # If key doesn't exist, None
    print(y)
    # Choice depends on how you want to handle errors
    print(in_dictionary.keys())
    print(in_dictionary.values())


def add_to_dictionary(in_dictionary, new_key, new_value):
    in_dictionary[new_key] = new_value


if __name__ == "__main__":
    my_dictionary = create_dictionary()
    print(my_dictionary)
    get_from_dictionary(my_dictionary)
    add_to_dictionary(my_dictionary, "drink", "swallowing a liquid")
    print(my_dictionary)

    x = {1: "first number", 2.3: "decimal key"}
    print(x)
    patient = {"name": "Ann", "test_results": [("HDL", 200), ("LDL", 150)]}
    print(patient["test_results"][0])
