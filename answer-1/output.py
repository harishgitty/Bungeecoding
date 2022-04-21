import pandas as pd
from pip import main
main = pd.read_csv("main1.csv")
main.head()
main.groupby('product_description')['price'].mean()
main["price_new"] = main['price'].fillna(
   main.groupby('product_description')['price'].transform("mean")
)
print(main)