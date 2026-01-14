import csv

with open("data.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","skill"])
    writer.writerow(["gowtham","python"])

with open("data.csv","r")as f:
    reader=csv.reader(f)
    for _ in reader:
        print(_)