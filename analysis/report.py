import pandas as pd

data = pd.read_csv("output/input.csv")

fig = data.age.plot.hist().get_figure()
fig.savefig("output/descriptive.png")


fig2 = data.sex.plot.bar().get_figure()
fig2.savefig("output/descriptive_sex.png")
