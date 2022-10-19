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


out_data_2 = {"a": 3,
              "b": 7}
r_2 = requests.post("http://127.0.0.1:5000/add_numbers",
                    json=out_data_2)
print(r_2.status_code)
print(r_2.text)
