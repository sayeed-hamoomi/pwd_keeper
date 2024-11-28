from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
load_dotenv()




a=os.getenv("secret_key")
key=Fernet(a)


def decrypt(p):
    return key.decrypt(p.decode())


def addpwd(conn,name,password):
    c= conn.cursor()
    encrypt_pwd=key.encrypt(password.encode())
    c.execute("INSERT INTO pwdkeeper  (name, password) VALUES (?,?)",(name,encrypt_pwd))
    conn.commit()
    return True
def viewpwd(conn):
    c= conn.cursor()
    c.execute("SELECT * FROM pwdkeeper") 
    res=c.fetchall()
    return res 

  
    