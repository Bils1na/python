import pandas as pd
import pathlib
from pathlib import Path


df = pd.read_csv("homework8/california_housing_train.csv")

print(df.query("population > 0 and population <= 500") ["median_house_value"].mean())