from IDatenbankverbindung import IDatenkbankverbidung

class Datenbankverbindung_Tankstelle(IDatenkbankverbidung):

    def insert_sql_command(self,name,plz):
        _sql_insert = "Insert into Ort (name,plz) values (%s,%s)"
        self._mycursor.execute(_sql_insert,[name,plz])
        self._mydb.commit()
