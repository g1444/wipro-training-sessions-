import mysql.connector
import pandas as pd
import numpy as np
from mysql.connector import Error

connection = None
df = None

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="company_db"
    )

    if connection is None or not connection.is_connected():
        raise Error("Database connection failed")

    query = "SELECT id, product, category, quantity, price FROM sales"
    df = pd.read_sql(query, connection)

    if df is None or df.empty:
        raise ValueError("No data retrieved from sales table")

    df["total_amount"] = df["quantity"] * df["price"]

    sales_values = df["total_amount"].to_numpy()

    max_sale = float(np.max(sales_values))
    min_sale = float(np.min(sales_values))
    avg_sale = float(np.mean(sales_values))

    print("Maximum Sale Value:", max_sale)
    print("Minimum Sale Value:", min_sale)
    print("Average Sale Value:", avg_sale)

    category_totals = df.groupby("category", as_index=True)["total_amount"].sum()
    print("\nTotal Sales per Category:\n", category_totals)

    overall_revenue = float(df["total_amount"].sum())
    print("\nOverall Revenue:", overall_revenue)

    print("\nFinal DataFrame:\n", df.to_string(index=False))

except mysql.connector.Error as db_error:
    print("Database Error:", db_error)

except ValueError as value_error:
    print("Data Error:", value_error)

finally:
    if connection is not None and connection.is_connected():
        connection.close()
