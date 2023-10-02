import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)
print()

one_hot = pd.DataFrame()

for value in data["whoAmI"].unique():
    one_hot[value] = (data["whoAmI"] == value).astype(int)

print(one_hot)
