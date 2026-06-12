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