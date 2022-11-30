import requests

# GET IDs for two patients (blood donor and recipient)
id_req = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/iww")
text_result = id_req.text
json_result = id_req.json()
donor_id = json_result["Donor"]
recipient_id = json_result["Recipient"]
print("Request to get patients for iww returns: {}".format(text_result))
print("Donor ID: {}".format(donor_id))
print("Recipient ID: {}".format(recipient_id))

# GET blood type of the two patients
req_donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"
                         + donor_id)
req_rec = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"
                       + recipient_id)
donor_bloodtype = req_donor.text
rec_bloodtype = req_rec.text
print("Donor Blood Type: {}".format(donor_bloodtype))
print("Recipient Blood Type: {}".format(rec_bloodtype))

# Calculate whether the recipient and donor are an acceptable match
match_result = "No"
if (donor_bloodtype == "O+"):
    if (rec_bloodtype == "A+" or
            rec_bloodtype == "B+" or
            rec_bloodtype == "AB+" or
            rec_bloodtype == "O+"):
        match_result = "Yes"
print("Is this a good match? {}".format(match_result))

# Check result with a POST request
info = {"Name": "iww", "Match": match_result}
check = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                      json=info)
print("Is the result correct or incorrect? {}".format(check.text))
