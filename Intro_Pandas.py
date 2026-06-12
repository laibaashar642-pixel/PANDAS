import pandas as pd
colleagues={
    "Name":["laiba","Ashar","Sana","Ali","Zainab"],
    "Age":[23,89,67,34,90],
    "Role":["Frontend","Backend","IT Manager","SQA","Tester"],
    
}
df=pd.DataFrame(colleagues)
print(df)
df.to_csv("Team.csv",index=False)
df.to_html("Team.html",index=False)
#df.to_excel("Team.xlsx",index=False) to use it we have to import the openpyx1

#Methods for dataframes
#it gives first top default values
print(df.head())
print(df.head(2))
#last end rows checks data ends in a cleanly way
print(df.tail(3))
#Returns the rows,columns your data size
print(df.shape)
#column names,types,non null counts,spot missing data instantly
print(df.info())
#Stats for number columns means,mix,max,std
print(df.describe())
#List of all columns,used for large datasets
print(df.columns)
#Add new column in exsisting one

df['Salary']=[5000,40000,300000,50000,20000]
print(df)
#Add a column based on logic
df['Senior']=df['Age']>40
print(df)
#Remove a column
df.drop(columns=['Senior'],inplace=True)
#Remove a row by index inplace=True means "change this DataFrame directly." Without it, Pandas returns a new copy and your original stays unchanged.
df.drop(index=2,inplace=True)
#Rename Columns
df.rename(columns={'Name':'Employee','Role':'Posistion'},inplace=True)