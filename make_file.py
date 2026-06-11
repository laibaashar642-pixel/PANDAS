#Pandas is an advanced version of excel we deal the data inn the form of columns first we mmake tables then store in differnet types of files like csv,excel,jsonmeans we make data frames
import pandas as pd
team_data={
    "Name":["Ayesha","Komal","Ali","Muskan","Laiba"],
    "Role":["Frotend Developer","Backened Developer","IT Manager","Product Manager","AI Intern"],

}
#This turns into table structure grid form
df=pd.DataFrame(team_data)
#print this data
print(df)
#If i wanted to save this excel data into csv file then i have to write this
df.to_csv("team.csv",index=False)
#If you have thousand of emails to read then you if try to open these 1000 emails then this freeze your screen therefore pandas give you efficiency by providing the methods to read top head 5 rows or 4 columns and also tail method and if we have not passed any value then it gives us first 5 and last 5 values simply we can extract the quick overview of our dataset heads help us to see the top where the tail helps usto see the ending of our dataset
#This method shows the top rows
print(df.head())
print(df.head(2))
print(df.head(7))
print(df.head(9))
print(df.head(10))
print(df.tail(10))

#It tells your shape of data means how many columns and rows exist in your table
print(df.shape)

#Filtering Method Like in orm,sql,indexing,searching
#To extract specific column
print(df['Name'])
print(df['Role'])

""" Rows ko Filter karna (Condition lagana):
Agar aapko sirf wo bache chahiye jinka score 90 se bada (> 90) hai, to aap Pandas ko aise batate hain: """
Status=df[df['Role']=='IT Manager']
print(Status)
#first we have to tell the which column and  table we have to look into and what to find
condition=df['Role']=='Frontend Developer'
#pass that condition inside the table to filter the data
frontend_workers=df[condition]
print(frontend_workers)
duplication=df[df["Name"]=='RANA']
print(duplication)
#Aggregation and grouping(data ka nichor) it helps to make grouping our data
#.value_counts() (Ginti karna)
print(df['Name'].value_counts())
print(df['Role'].value_counts())
designing=df["Name"]=='Laiba'
print(designing)
#To read any file from the pandas
#When we read the file then it returns the error in the form of encoding it is a process of converting into hidden text to avoid it we used encoding="utf-8","latin-1"
#If we have a data on cloud storage and we wanted to read it then we use the library of gcfs
""" df=pd.read_html("Practice_File")
print(df)  """
#We use info method to solve these problemscoulmns,row what type of? missing data info method() is used to for number of rows and columns column name int 64,float64 object non null counts info method is used to summarize our data
print(df.info())