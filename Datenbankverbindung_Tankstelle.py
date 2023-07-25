from IDatenbankverbindung import IDatenbankverbidung

class Datenbankverbindung_Tankstelle(IDatenbankverbidung):

    def insert_sql_command(self,name,plz):
        _sql_insert = "Insert into Ort (name,plz) values (%s,%s)"
        self._mycursor.execute(_sql_insert,[name,plz])
        self._mydb.commit()
    def delete_sql_command(self,Tid):
        _sql_delete = "Delete from Tankstelle where Tid = %s"
        self._mycursor.execute(_sql_delete,Tid)
        self._mydb.commit()
    def update_sql_command(self, Tid, name):
        _sql_update = "Update Tankstelle set name = %s where Tid = %s"
        self._mycursor.execute(_sql_update,[name,Tid])
        self._mydb.commit()
    def select_Tid_sql_command(self, name, plz):
        _sql_select = "select Tid from Tankstelle where name = %s and plz = %s"
        self._mycursor.execute(_sql_select,[name,plz])
        result = self._mycursor.fetchall()
        return result