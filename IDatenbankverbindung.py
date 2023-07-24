import mysql.connector

#https://www.w3schools.com/python/python_mysql_insert.asp

#Wenn folgender Fehler auftritt:
#Authentication plugin 'caching_sha2_password' is not supported

#Lösung: im Terminal:
#1. pip uninstall mysql-connector
#2. pip uninstall mysql-connector-python
#3. pip install mysql-connector-python

class IDatenbankverbidung():
    _mydb = ""
    _mycursor = ""
    def __init__(self,host,user,password,port,databasename):
        self._mydb = mysql.connector.connect(host=host,port=port,user=user,password=password,database=databasename,auth_plugin='mysql_native_password')
        self._mycursor = self._mydb.cursor()
        
    def insert_sql_command(self,sql,val):
        pass
    def select_sql_command(self):
        pass
    def delete_sql_command(self):
        pass
    def update_sql_command(self):
        pass
