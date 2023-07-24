from IDatenbankverbindung import IDatenbankverbidung

class Datenbankverbindung_Messung(IDatenbankverbidung):

    def insert_sql_command(self,Tid,datum,bezin,diesel,e10,superplus):
        _sql_insert = "Insert into Messung (Tid,datum,benzin,diesel,e10,superplus) values (%s,&s,%s,&s,%s,&s)"
        self._mycursor.execute(_sql_insert,[Tid,datum,bezin,diesel,e10,superplus])
        self._mydb.commit()
    def select_sql_command(self,Mid):
        _sql_select = "Select * from Messung where Mid = %s"
        self._mycursor.execute(_sql_select,Mid)
        self._mydb.commit()
    def delete_sql_command(self,Mid):
        _sql_delete = "Delete from Messung where Mid = %s"
        self._mycursor.execute(_sql_delete,Mid)
        self._mydb.commit()