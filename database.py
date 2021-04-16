import sqlite3
import hashlib
from datetime import datetime
filename = "tokensdatabase.db"
class TokensDB:
    def __init__(self,filename):
        self.connection = sqlite3.connect(filename)
        c = self.connection.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tokens' ''')
        if c.fetchone()[0]==1 : 
            pass
        else :
            c.execute('CREATE TABLE tokens (username TEXT, password TEXT, token TEXT)')		
            self.connection.commit()
        print("database connection successfully opened")
        self.connection.close()
    
    def generatetoken(self,uname,pwd):
        itext = uname+pwd+datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        return hashlib.md5(itext.encode()).hexdigest()

    def register(self,username,password):
        self.connection = sqlite3.connect(filename)
        c = self.connection.cursor()
        c.execute("SELECT count(*) FROM tokens WHERE username = '"+username+"' AND password = '"+password+"'")
        if c.fetchone()[0] == 0:
            t = self.generatetoken(username,password)
            c.execute("insert into tokens (username,password,token) values ('dileep','1234567890','"+t+"')")
            self.connection.commit()
            print("new user:")
            print("username: ",username)
            print("password: ",password)
        self.connection.close()

    def generate_token(self,username,password):
        self.connection = sqlite3.connect(filename)
        c = self.connection.cursor()
        c.execute("SELECT count(*) FROM tokens WHERE username = '"+username+"' AND password = '"+password+"'")
        if c.fetchone()[0] == 0:
            self.connection.close()
            return -1
        else:
            t = self.generatetoken(username,password)
            c.execute("update tokens set token='"+t+"' where username = '"+username+"' AND password = '"+password+"'")
            self.connection.commit()
            self.connection.close()
            print("generate token: ")
            print("username: ",username)
            print("password: ",password)
            return t

    def get_token(self,username,password):
        self.connection = sqlite3.connect(filename)
        c = self.connection.cursor()
        c.execute("SELECT count(token) FROM tokens WHERE username = '"+username+"' AND password = '"+password+"'")
        if c.fetchone()[0] == 0:
            self.connection.close()
            return -1
        else:
            c.execute("SELECT token FROM tokens WHERE username = '"+username+"' AND password = '"+password+"'")
            print("new user:")
            print("username: ",username)
            print("password: ",password)
            r = c.fetchone()[0]
            self.connection.close()
            return r


tdb = TokensDB("tokensdatabase.db")