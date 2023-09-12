import pandas as pd
import numpy as np

pd.options.display.max_columns = 20
pd.options.display.max_rows = 20
pd.options.display.max_colwidth = 80
np.set_printoptions(precision=4, suppress=True)

df = pd.read_json("pydata-book/datasets/usda_food/database.json")
print(df.head())

print(df["group"].describe())

#
# Pandas way to do a bar chart histogram for zip codes
#
# zip_counts = df.zip.value_counts()
# zip_counts.sort_index().plot.bar(xlabel="Zip Code", ylabel="Count", figsize=(14,2.4), legend=False)

#
# Seaborn way to do a bar chart histogram for zip codes
#
# import seaborn as sns
# from matplotlib import pyplot
# import matplotlib as plt
# pyplot.rc('axes', labelsize=18)
# plt.rcParams['figure.dpi'] = 150
# def figure_size_ax(width_in: float, height_in: float):
#     fig, ax = pyplot.subplots(figsize=(width_in, height_in))
#     return ax
# zip_plot = sns.countplot(data=df, x="zip", ax=figure_size_ax(14, 3), color="blue")
# zip_plot.set(xlabel="Zip Code", ylabel="Count")
# pyplot.setp(zip_plot.get_xticklabels(), rotation=90)
# zip_plot
