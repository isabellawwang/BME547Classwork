import requests

# output_info = {"name": "David Ward",
#               "net_id": "daw74",
#              "e-mail": "david.a.ward@duke.edu"}

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/iww")
print(r)
print(r.text)
