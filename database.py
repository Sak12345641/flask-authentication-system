import sqlite3
connection=sqlite3.connect("Logindata.db")
cursor=connection.cursor()
cmd1="""CREATE TABLE IF NOT EXISTS USERS(first_name varchar(50),
last_name varchar(50),
email varchar(50) primary key,
password varchar(50) not null
)"""
cursor.execute(cmd1)
cmd2="""INSERT INTO USERS VALUES("Sakshi","Mishra","sak@gmail.com","sak1234")"""
cursor.execute(cmd2)
connection.commit()
ans=cursor.execute("select*from USERS").fetchall()
for i in ans:
    print(i)