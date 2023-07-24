import mysql.connector

#https://www.w3schools.com/python/python_mysql_insert.asp

#https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported
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
