from IDatenbankverbindung import IDatenkbankverbidung

class Datenbankverbindung_Ort(IDatenkbankverbidung):

    def insert_sql_command(self,data):
        _sql_insert = "Insert into Ort (plz,name) values (%s,%s)"
        self._mycursor.execute(_sql_insert,data)
        self._mydb.commit()
    def delete_sql_command(self):
