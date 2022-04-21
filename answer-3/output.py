import pandas as pd
main = pd.read_csv("main3.csv")
teams = main[['Team','Yellow Cards','Red Cards']]
teams.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
print(teams)