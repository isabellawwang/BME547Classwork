def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 = Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            keep_running = False # optional, you could not include this 
            return

# note: accidentally named branch for this "HRL" insted of "HDL"
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

def HDL_driver(): # driver calls other functions and moves variables in between them
    HDL_value = input_HDL()
    HDL_characterization = check_HDL(HDL_value)
    output_HDL_result(hdl_value, answer)

def output_HDL_result(hdl_value, charac):
    print("The results for an HSL value of {} is {}".format(hdl_value, charac))

interface()
