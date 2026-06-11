#Pandas is an advanced version of excel we deal the data inn the form of columns first we mmake tables then store in differnet types of files like csv,excel,jsonmeans we make data frames
import pandas as pd
team_data={
    "Name":["Ayesha","Komal","Ali","Muskan"],
    "Role":["Frotend Developer","Backened Developer","IT Manager","Product Manager"],

}
#This turns into table structure grid form
df=pd.DataFrame(team_data)
#print this data
print(df)
#If i wanted to save this excel data into csv file then i have to write this
df.to_csv("team.csv",index=False)
#If you have thousand of emails to read then you if try to open these 1000 emails then this freeze your screen therefore pandas give you efficiency by providing the methods to read top head 5 rows or 4 columns
#This method shows the top rows
print(df.head)
print(df.head(2))
print(df.head(7))
#It tells your shape of data means how many columns and rows exist in your table
print(df.shape)
#Filtering Method
