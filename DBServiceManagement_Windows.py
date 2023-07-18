#https://stackoverflow.com/questions/46595845/python-command-to-stop-and-start-windows-services
import os
from IDBServiceManagement import IDBServiceManagement


class DBServiceManagement(IDBServiceManagement):

    def start_service(self,service):
        os.system(f'net start {service}')

    def stop_service(self,service):
        os.system(f'net stop {service}')