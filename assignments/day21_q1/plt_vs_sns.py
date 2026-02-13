months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]


import matplotlib.pyplot as plt

plt.plot(months, sales, marker='o', linestyle='--')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x=months, y=sales)

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.show()
