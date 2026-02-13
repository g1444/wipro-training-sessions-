import pandas as pd

# Read the sheet "2025"
df = pd.read_excel("data.xlsx")

# Add Total column
df["Total"] = df["Quantity"] * df["Price"]

# Save to new Excel file
df.to_excel("sales_summary.xlsx", index=False)


