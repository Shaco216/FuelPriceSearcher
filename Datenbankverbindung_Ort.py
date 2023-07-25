from IDatenbankverbindung import IDatenbankverbidung

class Datenbankverbindung_Ort(IDatenbankverbidung):

    def insert_sql_command(self,data):
        _sql_insert = "Insert into Ort (plz,name) values (%s,%s)"
        self._mycursor.execute(_sql_insert,data)
        self._mydb.commit()
    def delete_sql_command(self,plz):
        _sql_delete = f"Delete from Ort where %s"
        self._mycursor.execute(_sql_delete,plz)
        self._mydb.commit()
    def select_sql_command_plz(self,plz):
        _sql_select = f"Select * from Ort where plz = %s"
        self._mycursor.execute(_sql_select,plz)
        result = self._mycursor.fetchall()
        return result
    def select_sql_command_name(self,name):
        _sql_select = f"Select * from Ort where name = %s"
        self._mycursor.execute(_sql_select,name)
        result = self._mycursor.fetchall()
        return result
    def update_sql_command(self,newname,targetplz):
        _sql_update = f"Update Ort Set name = %s where plz = %s"
        self._mycursor.execute(_sql_update,[newname,targetplz])
        self._mydb.commit()