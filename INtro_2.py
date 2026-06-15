import pandas as pd
# team_makers={
#     'name':['Laiba','Ashar','Sana','Huma'],
#     'class':['It','Cs','Se','Ai'],
#     'skills':['Frontend','Backened','Networking','Mentorship'],

# }
# #Dataframe poori ki poori table ajye ghi
# df=pd.DataFrame(team_makers)
# print(df)
# #Series means aik column ki trah(Index+ value) kai sth
# """ df=pd.Series(team_makers)
# print(df) """
# #At a time we only have to used whether its series or dataframes
# #Commands in Pandas
# print(df.head())#Default First Five Rows
# print(df.tail())#Last five rows
# print(df.shape)#Means Table ki length
# print(df.info())#Data Type aur null values
# print(df.describe())#Numbers ki summary Mean ,max,min etc
# #Accessing Column
# print(df['name'])
# #print(df.age)

# #With the help of csv make dataframes
# df.to_csv('Student.csv',index=False)
# #To read any csv file
# #df=pd.read_csv('Students.csv')
# #Loc vs illoc Dono sai rows select krty hai but difference is whether its from label or number
# #Loc (label se)Index kai name se Illoc yani position se
# print(df.loc[1])#Index 1 label wali row
# print(df.loc[1:3])#label 1 sai 3 tk(With including of 3 index)
# print(df.loc[1,'name'])#Row 1 sirf name column Ashar
# print(df.iloc[2])
# print(df.iloc[0:3])
# print(df.iloc[1,2])
# # loc mein slice end include hota hai. iloc mein end exclude hota hai — exactly Python list jaisa.
# #Filtering Method In which you have to write only condition pandas automatically extract the rows condition bnayain gai aur ye sirf true wali values hi return kry gha
# df[df['class']=='It']
# print(df)
# #Multiple Conditions With And Or
# df[(df['class']=='Ai')|(df['name']=='Laiba')]
# print(df)
# # ZAROORI: har condition ke around () lagana zaroori hai!
# df[(df['class']=='Ai')&(df['name']=='Laiba')]
# print(df)
# #Multiple Columns Selection
# df[['name','skills']]

# # Filter + sirf kuch columns
# df[df['marks'] > 40][['name', 'marks']]

# # .query() — zyada clean tarika
# df.query('marks > 40 and age < 70')
# # String mein likho condition — quotes ke andar &/| ki jagah and/or
# #Data Transformation and Cleaning
""" 
NAN(Not A Number) bnanay kai liye """
import numpy as np
data={
    'name':['Laiba',np.nan,'Fiza','Zunaira'],
    'age':[23,90,np.nan,40],
    'marks':[np.nan,34,90,23]
}
df=pd.DataFrame(data)
#Methods to check 
print(df.isnull)#her cell true false hai ya nahi ya NAN hai
print(df.isnull().sum())#hr column mai kitny nan hai
print(df.dropna())#Jo bhi row mai aik bhi nan ho usko delete krdo
print(df.dropna(subset=['marks']))#Sirf marks wali nan drop kro
print(df.fillna(0))#sb nan ko zero se bharo
print(df.fillna({'marks': df['marks'].mean()}, inplace=True))#marks kai nan ko marks ki average sai bhar doa
#Columns  Renaming and Modification
#Rename
df.rename(columns={"marks":"score","age":"years"},inplace=True)
#Adding new column
df['passing']='Yes'#Sb ko yes
df['total']=df['score']*2 #marks ko double
#Exsisting Column Modification
df['score']=df['score']+5
#You can't apply all the operations so choose one by one
#Apply Aur Lambda
#Apply means hr value pr aik function chalo
def grade_marks(marks):
    if marks>80: return "Pass"
    elif marks<90: return "Fail"
    elif marks<70: return "Fail"
    else:
        return "Average"
    