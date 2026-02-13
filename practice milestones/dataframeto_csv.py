import pandas as pd

data = {
    "Name": ["Gowtham", "Arun", "Priya", "Sneha", "Karthik"],
    "Maths": [85, 78, 92, 88, 74],
    "Science": [90, 80, 95, 85, 70],
    "English": [75, 82, 89, 90, 76],
    "Total": [250, 240, 276, 263, 220]
}

df = pd.DataFrame(data)

file_path = "marks.csv"
df.to_csv(file_path, index=False)

file_path
