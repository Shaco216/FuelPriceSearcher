from IDatenbankverbindung import IDatenbankverbidung

class Datenbankverbindung_Messung(IDatenbankverbidung):

    def insert_sql_command(self,Tid,datum,benzin):
        _sql_insert = "Insert into Messung (Tid,datum,benzin) values (%s,&s,%s)"
        self._mycursor.execute(_sql_insert,[Tid,datum,benzin])
        self._mydb.commit()
    def select_sql_command(self,Mid):
        _sql_select = "Select * from Messung where Mid = %s"
        self._mycursor.execute(_sql_select,Mid)
        result = self._mycursor.fetchall()
        return result
    def delete_sql_command(self,Mid):
        _sql_delete = "Delete from Messung where Mid = %s"
        self._mycursor.execute(_sql_delete,Mid)
        self._mydb.commit()
    def insert_sql_command_benzin(self,Tid,datum,benzin):
        _sql_insert = "Insert into Messung (Tid,datum,benzin) values (%s,&s,%s)"
        self._mycursor.execute(_sql_insert,[Tid,datum,benzin])
        self._mydb.commit()