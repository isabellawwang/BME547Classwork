import requests

# Insert URL that you want to make a request to
r = requests.get("https://api.github.com/repos/"
                 + "isabellawwang/BME547Classwork/braniiwoaeches")

print(r)
print(r.text)
if r.status_code == 200:
    answer = r.json()
    print(type(answer))
    for branch in answer:
        print(branch["name"])
else:
    print("Bad request: {}".format(r.text))
