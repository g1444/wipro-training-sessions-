import json
data={"name":"gowtham","age":21,"course":"IT"}

with open("data.json","w") as f:
    json.dump(data,f)

with open("data.json","r") as f:
    content=json.load(f)
    print(content)