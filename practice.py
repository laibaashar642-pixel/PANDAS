# 5 students ka DataFrame banao jisme columns hon: name, age, marks. Phir print karo.
import pandas as pd
Students={
    'name':['Laiba','Ashar','Fiza','Zunaira','Ali'],
    'age':[23,90,67,40,50],
    'marks':[20,56,89,47,39],
}
df=pd.DataFrame(Students)
print(df)
# Upar wale DataFrame ka shape, info() aur describe() print karo. Har ek ka output samjho.
print(df.shape)
print(df.info())
print(df.describe())
print(df['name'])
print(df['age'])
print(df.head(3))
print(df.tail(2))