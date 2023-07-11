import mysql.connector

class IDatenkbankverbidung():
    _mydb = ""
    _sqlcommand = ''

    def __init__(self,host,user,password):
        self._mydb = mysql.connector.connect(host=host,user=user,password=password)
    def do_sql_command(self):
        pass