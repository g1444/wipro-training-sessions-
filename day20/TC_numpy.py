import numpy as np
import pandas as pd

arr=np.array([1,3,4,5,6,9])
print("array:",arr)
print("sum: ",np.sum(arr))
print("mean; ",np.mean(arr))
print("multiply: ",arr*2)

data={
    "name": ["kiran","anita","ravi"],
    "age":[25,27,26],
    "city":["Banglore","chennai","Hyderabad"]

}
df=pd.DataFrame(data)
print(df)

print(df["name"])
print(df[df["age"]>26])
df["salary"]=[50000,70000,60000]

print(df)