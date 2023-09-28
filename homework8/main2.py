import pandas as pd

df = pd.read_csv("homework8/california_housing_train.csv")
temp = df["population"].min() * 1.45

print(df.query(f"population > {temp}") ["households"].max())