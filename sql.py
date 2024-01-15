import sqlite3

# Connect to database
connection = sqlite3.connect("student.db")

# Create a cursor for inserting records, fetching data etc.
cursor = connection.cursor()

# Create table
table_info = """
Create table STUDENT(NAME varchar(50), CLASS varchar(50), DIVISION varchar(50), MARKS int);
"""
cursor.execute(table_info)

# Insert Some more records

cursor.execute(''' Insert into STUDENT values("Shiva", "Data Science" , "A" , 90) ''')
cursor.execute(''' Insert into STUDENT values("kavita", "Data Science" , "A" , 85) ''')
cursor.execute(''' Insert into STUDENT values("Shankar", "Data Engineer" , "A" , 80) ''')
cursor.execute(''' Insert into STUDENT values("Viresh", "Data Science" , "B" , 96) ''')
cursor.execute(''' Insert into STUDENT values("Sada", "Data Analyst" , "A" , 99) ''')
cursor.execute(''' Insert into STUDENT values("Ramesh", "PowerBI" , "B" , 78) ''')

# Display all records
print("Inserted values are: ")
data = cursor.execute(""" Select *from STUDENT """)
for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
