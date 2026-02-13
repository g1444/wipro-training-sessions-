import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "score": [85, 92, 78, 90, 88]
}

df = pd.DataFrame(data)

mean_score = np.mean(df["score"])
median_score = np.median(df["score"])
std_score = np.std(df["score"], ddof=1)

df["above_average"] = df["score"] > mean_score

print(df)
print("mean:", mean_score)
print("median:", median_score)
print("standard deviation:", std_score)
