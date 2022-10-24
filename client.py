# client.py

import requests


""" r = requests.get("http://127.0.0.1:5000/info")
print(r.status_code)
print(r.text) """


""" out_data = {"name": "David Ward",
            "hdl_value": 30}
r = requests.post("http://127.0.0.1:5000/hdl_check",
                  json=out_data)
print(r.status_code)
print(r.text) """


out_data_2 = {"c": 3,
              "d": 7}
r_2 = requests.post("http://127.0.0.1:5000/add_numbers",
                    json=out_data_2)
print(r_2.status_code)
print(r_2.text)


r = requests.get("http://127.0.0.1:5000/add/2/3")
print(r.status_code)
print(r.text)
