import mysql.connector

#https://www.w3schools.com/python/python_mysql_insert.asp
class IDatenkbankverbidung():
    _mydb = ""
    _mycursor = ""
    def __init__(self,host,user,password,database):
        self._mydb = mysql.connector.connect(host=host,user=user,password=password,database=database)
        self._mycursor = self._mydb.cursor()
        
    def insert_sql_command(self,sql,val):
        pass
    def select_sql_command(self):
        pass
    def delete_sql_command(self):
        pass
    def update_sql_command(self):
        pass