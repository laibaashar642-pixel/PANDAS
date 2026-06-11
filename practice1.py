import pandas as pd
data_sets={
    "Name":["Laiba","Ashar","Fiza","Umar","Waleed","Romeo"],
    "Age":["19","21","90","89","12","34"]
}
df=pd.DataFrame(data_sets)
print(df)
df.to_excel("Hello",index=False)