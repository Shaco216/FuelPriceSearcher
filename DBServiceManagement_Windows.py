#https://stackoverflow.com/questions/46595845/python-command-to-stop-and-start-windows-services
import os
from IDBServiceManagement import IDBServiceManagement
#windows service running check
#https://stackoverflow.com/questions/46579170/python-code-to-check-if-service-is-running-or-not
class DBServiceManagement(IDBServiceManagement):

    def start_service(self,service):
        os.system(f'net start {service}')

    def stop_service(self,service):
        os.system(f'net stop {service}')

    def check_service_is_running(self,service):
        stat = os.system(f'service {service} status')
        return stat