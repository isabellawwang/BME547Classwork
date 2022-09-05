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

def input_HDL():
    user_HDL = input("Enter the HDL value: ")
    return int(user_HDL) # convert string into integer so you can better work with it later
    
interface()
num = input_HDL()