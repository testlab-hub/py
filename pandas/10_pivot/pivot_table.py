# PIVOT Table
import pandas as pd

df = pd.read_csv("weather2.csv")
# print(df)

example_1 = df.pivot_table(index="city", columns="date")
example_2 = df.pivot_table(index="city", columns="date", aggfunc="sum")
example_3 = df.pivot_table(index="city", columns="date", aggfunc="count")
print(df)
print("*************************************************")
print(example_1)
print("*************************************************")
# https://numpy.org/doc/stable/reference/routines.math.html
print(example_2)
print("*************************************************")
print(example_3)
