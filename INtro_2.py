import pandas as pd
team_makers={
    'name':['Laiba','Ashar','Sana','Huma'],
    'class':['It','Cs','Se','Ai'],
    'skills':['Frontend','Backened','Networking','Mentorship'],

}
#Dataframe poori ki poori table ajye ghi
df=pd.DataFrame(team_makers)
print(df)
#Series means aik column ki trah(Index+ value) kai sth
df=pd.Series(team_makers)
print(df)
#Commands in Pandas
print(df.head())#Default First Five Rows
print(df.tail())#Last five rows
print(df.shape)#Means Table ki length
print(df.info())#Data Type aur null values
print(df.describe())#Numbers ki summary Mean ,max,min etc
#Accessing Column
print(df['name'])
#print(df.age)

#With the help of csv make dataframes
df.to_csv('Student.csv',index=False)
#To read any csv file
#df=pd.read_csv('Students.csv')
