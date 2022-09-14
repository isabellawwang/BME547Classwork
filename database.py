from venv import create


# September 14th class
# Working with lists

# Functions are useful for changing code later
def create_patient_entry(patient_name, patient_id, patient_age):
    # Makes a list with patient information and empty list for test results
    new_patient = [patient_name, patient_id, patient_age, []] 
    return new_patient

def print_patient(patient_info):
    print("Name: {}, ID: {}, Age: {}".format(patient_info[0], patient_info[1], patient_info[2]))

def print_database(my_database):
    for patient in my_database:
        print("---------------------------")
        print_patient(patient)

def find_patient_by_id(my_database, id_to_find):
    for patient in my_database:
        if patient[1] == id_to_find:
            print("FINDING PATIENT...")
            print_patient(patient)
            return patient
    return False

def add_test_results(my_database, p_id, test_name, test_value):
    patient = find_patient_by_id(my_database, p_id)
    if patient == False:
        return False
    patient[3].append((test_name, test_value)) # Adding a tuple
    print("ADDING TEST RESULTS...")
    print("Patient edited:")
    print_patient(patient)
    print("Test results added: {}".format(patient[3]))
    return patient

def main():
    db = [] # database list
    db.append(create_patient_entry("Ann Ables", 1, 30)) # Create a patient entry for Ann Ables
    db.append(create_patient_entry("Bob Boyles", 2, 34)) # Create a patient entry for Bob Boyles
    db.append(create_patient_entry("Chris Chou", 3, 25)) # Create a patient entry for Chris Chou
    print("My database:", db) # Print the patient entry
    print("Chris Chou's age:", db[-1][-2]) # Print Chris Chou's age
    print("First two items of list:", db[0:2]) # Print first two items in list
    print("Chris Chou's first name:", db[-1][0][:5]) # Print Chris Chou's first name

    print_database(db)
    find_patient_by_id(db, 1)
    find_patient_by_id(db, 2)
    find_patient_by_id(db, 3)

    add_test_results(db, 1, "HDL", "100")

    room_list = ["Room 1", "Room 2", "Room 3"]
    
    for i, patient in enumerate(db): # i = which index I'm on
        print("Name = {}, Room = {}".format(patient[0], room_list[i]))
    
    for patient, room in zip(db, room_list):
        print("Name = {}, Room = {}".format(patient[0], room))

if __name__ == "__main__":
    main()