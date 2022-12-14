from venv import create


# September 14th class
# Working with lists

# Functions are useful for changing code later

"""
def create_patient_entry(patient_name, patient_id, patient_age):
    # Makes a list with patient information and empty list for test results
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient
"""


def create_patient_entry(patient_first, patient_last, patient_id, patient_age):
    new_patient = {"First Name": patient_first,
                   "Last Name": patient_last,
                   "Id": patient_id,
                   "Age": patient_age,
                   "Tests": []}
    return new_patient


"""
def print_patient(patient_info):
    print("Name: {}, ID: {}, Age: {}".
          format(patient_info[0], patient_info[1], patient_info[2]))
"""


def print_patient(patient_dict):
    print("Name: {}, ID: {}, Age: {}".
          format(get_full_name(patient_dict),
                 patient_dict["Id"],
                 patient_dict["Age"]))


"""
def print_database(my_database):
    for patient in my_database:
        print("---------------------------")
        print_patient(patient)
"""


def print_database(db):
    for patient_key in db:
        print(patient_key)
        print("Name: {}, id: {}, age: {}".
              format(get_full_name(db[patient_key]),
                     db[patient_key]["Id"],
                     db[patient_key]["Age"]))


def get_full_name(patient):
    patient_first_name = patient["First Name"]
    patient_last_name = patient["Last Name"]
    full_name = patient_first_name + " " + patient_last_name
    return full_name


def find_patient_by_id(my_database, id_to_find):
    patient = my_database[id_to_find]
    return patient


def add_test_results(my_database, p_id, test_name, test_value):
    patient = find_patient_by_id(my_database, p_id)
    patient["Tests"].append((test_name, test_value))  # Adding a tuple
    print("ADDING TEST RESULTS...")
    print("Patient edited:")
    print_patient(patient)
    print("Test results added: {}".format(patient["Tests"]))
    return patient


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


def main():
    db = {}  # database list
    # Create a patient entry for Ann Ables
    db[1] = (create_patient_entry("Ann", "Ables", 1, 30))
    # Create a patient entry for Bob Boyles
    db[2] = (create_patient_entry("Bob", "Boyles", 2, 34))
    # Create a patient entry for Chris Chou
    db[3] = (create_patient_entry("Chris", "Chou", 3, 25))
    # print("My database:", db)  # Print the patient entry
    print_database(db)
    print("Chris Chou's age:", db[3]["Age"])  # Print Chris Chou's age
    # Print first two items in list
    # print("First two items of dictionary:", db[0:2])
    # Print Chris Chou's first name
    # print("Chris Chou's first name:", db[-1]["First Name"])

    # print_database(db)
    find_patient_by_id(db, 1)
    find_patient_by_id(db, 2)
    find_patient_by_id(db, 3)

    add_test_results(db, 1, "HDL", "100")

    room_list = ["Room 1", "Room 2", "Room 3"]

    # for i, patient in enumerate(db):  # i = which index I'm on
    #    print("Name = {}, Room = {}".format(patient[0], room_list[i]))

    # for patient, room in zip(db, room_list):
    #    print("Name = {}, Room = {}".format(patient[0], room))

    print("Patient {} is a {}".format(get_full_name(db[2]),
                                      adult_or_minor(db[2])))


if __name__ == "__main__":
    main()
