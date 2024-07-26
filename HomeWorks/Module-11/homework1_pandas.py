import pandas as pd

df = pd.read_csv("IHME-GBD_2019_DATA-ff08d9bc-1.csv")
injuries = df[
    (df["location"] == "Russian Federation") & (df["sex"] == "Male") & (df["cause"] == "Unintentional injuries") & (
            df["val"] > 10)]
print(df.info())
arr = df["cause"].unique()
print(arr)
injuries = injuries.sort_values(by=["year"], ascending=True)
injuries = injuries.drop(columns=["metric", "upper", "lower"], axis=1)
injuries['value'] = injuries["val"].round(decimals=2)
injuries = injuries.drop(columns=["val"], axis=1)

injuries.to_csv("injuries.csv", sep=";", decimal=",")
df_cause = df.groupby('cause').agg({
    'year': ['count'], 'val': ['mean', 'median']})
print(df_cause['val']['mean'].sort_values(ascending=False))

df_pivot = df.pivot_table(values="val", index="location", columns="cause", aggfunc="mean", margins=False, dropna=True,
                          fill_value=None)
dfp = pd.DataFrame(df_pivot).T
dfp.to_csv("pivot_table.csv", sep=";", decimal=",", float_format="%.2f")
