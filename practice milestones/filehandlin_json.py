import json
with open("data.json","r") as f:
    loader=json.load(f)
    print(loader)
loader['name']= "varsha"
loader["age"]=21

print(loader)

with open("data.json","w") as f:
    json.dump(loader,f,indent=4)