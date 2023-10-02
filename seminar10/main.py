import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("seminar10/california_housing_train.csv")

print(df.head())


# sns.scatterplot(data=df, x="longitude", y="latitude")
# sns.scatterplot(data=df, x="population", y="households", hue="median_house_value")
# sns.scatterplot(data=df, x="longitude", y="latitude", hue = "housing_median_age", size="median_house_value")
# sns.scatterplot(data=df, x="longitude", y="latitude", hue="median_house_value")

# cols = ["population", "median_income", "housing_median_age", "median_house_value"]
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)

# sns.relplot(x="longitude", y="median_house_value", kind="line", data=df)

# sns.histplot(data=df, x="housing_median_age")
# sns.histplot(data=df[(df["housing_median_age"]<15) & (df["housing_median_age"]>0)], x="median_income")
# sns.histplot(data=df, x="population", binwidth=500)

df.loc[df["housing_median_age"] <= 20, "age_group"] = "new"
df.loc[(df["housing_median_age"] > 20) & (df["housing_median_age"] <= 50), 
       "age_group"] = "average"
df.loc[df["housing_median_age"] > 50, "age_group"] = "old"

print(df.head())
print(df["age_group"].value_counts())
age = df["age_group"].value_counts()
for i in range(len(age)):
    print(age[i] / age.sum() * 100)

df.groupby("age_group")["median_income"].mean().plot(kind="bar")

df["income_group"] = "poor"
df.loc[df["median_income"] > 5, "income_group"] = "rich"
df.loc[(df["median_income"] <= 5) & (df["median_income"] > 2), "income_group"] = "average"

# sns.histplot(data=df, x="income_group")
# sns.displot(df, x="median_house_value", hue="income_group")
sns.displot(df, x="median_house_value", hue="age_group")

# corr = df.corr()
# mask = np.triu(np.ones_like(corr, dtype=bool))
# f, ax = plt.subplots(figsize=(11, 9))
# cmap = sns.diverging_palette(230, 20, as_camp=True)

# sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
#             square=True, linewidths=.5, cbar_kws={"shrink": .5})


plt.show()