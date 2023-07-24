

class DBConnDataGatherer():
    _host = ""
    _user = ""
    _port = 0
    _password = ""
    _dbName = ""

    def set_host(self, hostname="localhost"):
        self._host = hostname
    def set_user(self,user="root"):
        self._user = user
    def set_port(self,port=3306):
        self._port = int(port)
    def set_password(self,password="root"):
        self._password = password
    def set_dbName(self,dbName="fuelpricesearcher"):
        self._dbName = dbName
    def set_default(self):
        self.set_host()
        self.set_user()
        self.set_port()
        self.set_password()
        self.set_dbName()
    def get_host(self):
        return self._host
    def get_user(self):
        return self._user
    def get_port(self):
        return self._port
    def get_password(self):
        return self._password
    def get_dbName(self):
        return self._dbName
    def get_all_settings(self):
        return [self._host,self._user,self._port,self._password,self._dbName]