# BME 547 Lecture 3
# September 5, 2022
# Author: Dr. David Ward; Isabella Wang

def input_HDL():
    user_HDL = input("Enter the HDL value: ")
    return int(user_HDL) # convert string into integer so you can better work with it later

def check_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif HDL >= 40: # you could also do 40 <= HDL_value <60
        return "Borderline Low"
    else:
        return "Low"

def output_HDL_result(hdl_value, hdl_charac):
    print("The result for an HDL value of {} is {}".format(hdl_value, hdl_charac))

def HDL_driver(): # driver calls other functions and moves variables in between them
    HDL_value = input_HDL()
    HDL_characterization = check_HDL(HDL_value)
    output_HDL_result(HDL_value, HDL_characterization)

def input_LDL():
    user_LDL = input("Enter the LDL value: ")
    return int(user_LDL)

def check_LDL(LDL):
    if LDL < 130:
        return "Normal"
    elif LDL <= 159:
        return "Borderline High"
    elif LDL <= 189:
        return "High"
    else:
        return "Very High"

def output_LDL_result(ldl_value, ldl_charac):
    print("The result for an LSL value of {} is {}.".format(ldl_value, ldl_charac))

def LDL_driver():
    LDL_value = input_LDL()
    LDL_characterization = check_LDL(LDL_value)
    output_LDL_result(LDL_value, LDL_characterization)

def input_total_chol():
    my_HDL = input("Enter the HDL value: ")
    my_LDL = input("Enter the LDL value: ")
    sum = int(my_HDL) + int(my_LDL)
    return sum

def check_total_chol(total):
    if total < 200:
        return "Normal"
    elif total <= 239:
        return "Borderline High"
    else:
        return "High"

def output_total_chol(chol_sum, chol_charac):
    print("The result for LDL + HDL = {} is {}.".format(chol_sum, chol_charac))

def total_chol_driver():
    total_value = input_total_chol()
    total_charac = check_total_chol(total_value)
    output_total_chol(total_value, total_charac)

def interface():
    print("Welcome to the Blood Calculator!")
    print("Here are your options:")
    print("1 - Analyze HDL") # Run HDL Driver
    print("2 - Analyze LDL") # Run LDL Driver
    print("3 - Estimate total cholesterol (HDL + LDL)")
    print("9 = Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            keep_running = False # optional, you could not include this 
            return
        elif choice == "1": # HDL
            HDL_driver()
        elif choice == "2": # LDL
            LDL_driver()
        elif choice == "3": # Estimate total (HDL + LDL)
            total_chol_driver()

if __name__ == "__main__":
    interface()
