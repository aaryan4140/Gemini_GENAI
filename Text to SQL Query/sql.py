import sqlite3

##connect to sqlite
connection= sqlite3.connect("student.db")

## create a cursor object to insert records, create table, retrive data
cursor= connection.cursor()

##create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

#insert records into database table

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

#display all the records
print("the inserted records are")

data=cursor.execute('''select * from STUDENT''')

for row in data :
    print(row)

## close the connection
connection.commit()
connection.close()






