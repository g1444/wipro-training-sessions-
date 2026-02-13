import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "OrderID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Quantity": [1, 2, 1, 1, 3],
    "UnitPrice": [800, 20, 50, 300, 20],
    "OrderDate": pd.date_range("2024-01-01", periods=5)
}

df = pd.DataFrame(data)

df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

category_sales = df.groupby("Category")["TotalSales"].sum()
average_order_value = df["TotalSales"].mean()

sales_values = df["TotalSales"].to_numpy()

print("Maximum Sales Value:", float(np.max(sales_values)))
print("Minimum Sales Value:", float(np.min(sales_values)))
print("Mean Sales Value:", float(np.mean(sales_values)))

print("\nCategory-wise Sales:\n", category_sales)
print("\nAverage Order Value:", float(average_order_value))

plt.figure()
category_sales.plot(kind="bar")
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

plt.figure()
sns.lineplot(x=df["OrderID"], y=df["TotalSales"])
plt.title("Order-wise Sales Trend")
plt.xlabel("Order ID")
plt.ylabel("Sales Value")
plt.tight_layout()
plt.show()

with pd.ExcelWriter("sales_report.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Raw_Data", index=False)
    category_sales.to_excel(writer, sheet_name="Category_Summary")
