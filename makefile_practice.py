import pandas as pd
#Make datasets
Collegue_Data={
    "Name":["Laiba","Ali","Zara","Sana"],
    "Profession":["AI Intern","Frontend","Backend","IT Manager"],
}
#Convert this table into dataframes
df=pd.DataFrame(Collegue_Data)
print(df)
#If we have to convert this file into json,excel then we do this
df.to_html("Practice_File",index=False)
import pandas as pd

# CHALLENGE: Add your favorite food to the list below!
my_data = {
    "Friend": ["Ayesha", "Sagar"],
    "Favorite_Food": ["Biryani", "__Quorma_____"]  # <-- Put a food name here!
}

# 1. Turn 'my_data' into a Pandas DataFrame table here:
df = pd.DataFrame(my_data)

# 2. Print your table to see how it looks:
print(df)
print(df.head)
print(df.head(7))
print(df.head(9))
print(df.shape)
import pandas as pd

# A table of student exam records
exam_data = {
    "Student_Name": ["Ayesha", "Maria", "Nida", "Hira", "Samia", "Zainab", "Ali"],
    "Score": [94, 93, 92, 87, 95, 78, 85],
    "Grade": ["A", "A", "A", "B", "A", "C", "B"]
}

df = pd.DataFrame(exam_data)
print(df)
