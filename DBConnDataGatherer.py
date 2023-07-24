

class DBConnDataGatherer():
    _host = ""
    _user = ""
    _port = 0
    _password = ""

    def set_host(self, hostname="localhost"):
        self._host = hostname
    def set_user(self,user="root"):
        self._user = user
    def set_port(self,port=3306):
        self._port = port
    def set_password(self,password="root"):
        self._password = password
    def set_default(self):
        self.set_host()
        self.set_user()
        self.set_port()
        self.set_password()
    def get_host(self):
        return self._host
    def get_user(self):
        return self._user
    def get_port(self):
        return self._port
    def get_password(self):
        return self._password
    def get_all_settings(self):
        return [self._host,self._user,self._port,self._password]