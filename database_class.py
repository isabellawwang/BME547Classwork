class Patient:

    # def __init__(self, first_name, last_name, patient_id, age):
    def __init__(self):  # __init__ defined within python
        self.first_name = ""
        self.last_name = ""
        self.patient_id = ""
        self. age = ""
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_first_name,
                         patient_last_name, patient_id,
                         patient_age):
    new_patient = Patient()
    new_patient.first_name = patient_first_name,
    new_patient.last_name = patient_last_name,
    new_patient.patient_id = patient_id,
    new_patient.age = patient_age
    return new_patient


def main():
    x = Patient()
    x.first_name = "Isabella"
    x.last_name = "Wang"
    print(x.last_name)

    y = Patient()
    y.first_name = "David"
    y.last_name = "Ward"
    print(y.last_name)
    print(type(x))
    print(type(y))
    exit()


if __name__ == "__main__":
    main()
