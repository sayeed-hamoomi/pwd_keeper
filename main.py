import sqlite3
from utils import addpwd,viewpwd, decrypt

conn = sqlite3.connect("pwdkeeper.db")
c = conn.cursor()

c.execute("CREATE TABLE  IF NOT EXISTS  pwdkeeper(id INTEGER PRIMARY KEY,name TEXT NOT NULL,password TEXT NOT NULL)")

print("menu \n 1. save\n 2. view ")



option=int(input("select an option:"))



if option==1:
    name=input("enter the name:")
    password=input("enter the password:")
    suc=addpwd(conn, name,password)
    if suc:
        print("added")
    else:
        print("not")

if option==2:
    res=viewpwd(conn)
    for i in res:
        print(f"Key: {i[1]}, Password: {decrypt(i[2])}")


    
    



conn.commit()
conn.close()

