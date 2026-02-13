import csv
highest_marks=0
with open("marks.csv","r") as f:
    reader=csv.DictReader(f)
    for _ in reader:
        total=int(_["Total"])

        if total>highest_marks:
            highest_marks=total
            topper_name=_["Name"]
print(f"the topper is {topper_name} with the total of {highest_marks}")

