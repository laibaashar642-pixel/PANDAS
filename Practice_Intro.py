"""Create a DataFrame of 5 students with columns: Name, Marks, City. Then print its shape, column names, and data types.
hint: use df.shape, df.columns, df.dtypes """
import pandas as pd
Students={
    "Name":["Laiba","Ashar","Sana","Ali","Sobhan"],
    "Marks":[23,45,90,56,12],
    "City":["lahore","Karachi","Faislabad","Bangladesh","Qatar"],

}
df=pd.DataFrame(Students)
print(df)
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
""" Add a new column called "Passed" — it should be True if Marks > 50, False otherwise.
hint: df['Passed'] = df['Marks'] > 50 """
df['Passed']=df["Marks"] > 50 

# Drop the "City" column from your DataFrame using drop().drop method also need to know whether you are droping the column or any row
print(df.drop(columns=("City"),inplace=True))
# Rename the "Name" column to "Student" and "Marks" to "Score".,When you rename the columns then you have to also save it
df.rename(columns={"Name":"Student","Marks":"Score"})
print(df.columns)

""" What happens if you do df['Marks'] + 10? Does it change the DataFrame? How do you make it permanent?
hint: think about inplace vs assignment """
#if i can do this may be in my thinking it adds the value 10 into the marks
#Now we had made the datasets then we did filtering of our datasets
"""  selecting columns
Think of columns like drawers in a cabinet. You pick one drawer by name, or grab multiple drawers at once. """
#Single Column Extracting is called series whether the multiple column series called dataframe
df['Marks']
df[['Name','Marks']]
# why double brackets? outer [] = indexing, inner [] = the list of columns
print(df)
""" Imagine a building. loc = find the office by its name/label. iloc = find the office by its floor number (position). Same building, different way to navigate. 
loc — by LABEL
Uses the actual index label or column name

df.loc[2] → row where index=2            iloc — by POSITION
Uses 0,1,2... position numbers only

df.iloc[2] → 3rd row (position 2)
df.iloc[2, 0] → row 3, col 1 = Sana
df.iloc[0:2] → rows 0,1 (exclusive!)
df.loc[2, 'Name'] → Sana
df.loc[0:2] → rows 0,1,2 (inclusive!)"""
 # row with index label 2 → Sana's row
df.loc[2]
#One cell
df.loc[2,'Name']
df.loc[0:3, 'Name':'Marks']  # rows 0-3, cols Name to Marks

""" df.iloc[2,0]
df.iloc[0:3,0:2]
df.iloc[0:3, 'Name':'Marks']   """
# rows 0-3, cols Name to Marks
df.iloc[2]                   # 3rd row by position → Sana's row
df.iloc[2, 0]                # row 3, column 1 → 'Sana'
df.iloc[0:3, 0:2]            # rows 0,1,2 — cols 0,1 (stop before 3,2)
""" key difference: loc[0:3] includes row 3. iloc[0:3] stops before row 3. loc is inclusive, iloc is exclusive at the end — just like Python lists. """
# filtering with conditions
""" A condition is a question you ask about every row. Pandas goes through each row, answers True or False, then returns only the True ones. """
condition=df[df["Marks"]>50]
print(condition)
condition_1=df[df["Name"]=="Laiba"]
print(condition_1)
#We can check the conditions like the sql
"""  multiple conditions
Want students from Lahore AND who passed? Chain conditions. Use & for AND, | for OR. Never use Python's and/or — they break in Pandas. """
condition_3=df[(df['City'] == 'Lahore') | (df['Marks'] > 80)]
print(condition_3)
