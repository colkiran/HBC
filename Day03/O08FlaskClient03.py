import json

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getplayers/ponting")

print(response)
print(response.json())

res = response.json()
for k, v in res.items():
    print(k, "=>", v)

print("put".center(60, "-"))

response = requests.put(BASE + 'getplayers/sachin', data = {'team': 'australia'})
res = response.json()
print(res)

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for ky, vl in info.items():
        print(ky, "=>", vl)


print("patch".center(60, "-"))
data = {'name': 'Sachin Ramesh Tendulkar'}
response = requests.patch(BASE + "getplayers/sachin", json=json.dumps(data))
res = response.json()

print(res)
for k, v in res.items():
    print(k, "=>", v)


print("post".center(60, "-"))
virat = {'name': 'Virat Kholi', 'age': 24, 'odi': 4300, 'test': 3700, 't20': 2000}

response = requests.post(BASE + "getplayers/virat", json=json.dumps(virat))
res = response.json()


for k, v in res.items():
    print(k, "=>", v)
    print("-" * 60)

print("delete".center(60, "-"))

response = requests.delete(BASE + "getplayers/lara")
res = response.json()

for ky, vl in res.items():
    print(ky)
    print(ky, "=>", vl)

