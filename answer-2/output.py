import pandas as pd
main = pd.read_csv("main2.csv")
main.head()
main["sales_amount"]=main["sales_quantity"].where(
    main["unit"]!="pcs",
    main["product_description"].str.split("-",expand=True)[1].astype("float")*\
    main["sales_quantity"]
)
print(main)