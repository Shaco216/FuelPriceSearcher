#https://stackoverflow.com/questions/46595845/python-command-to-stop-and-start-windows-services
import os
import subprocess
from IDBServiceManagement import IDBServiceManagement
#windows service running check
#https://stackoverflow.com/questions/46579170/python-code-to-check-if-service-is-running-or-not

#todo: https://stackoverflow.com/questions/21944895/running-powershell-script-within-python-script-how-to-make-python-print-the-pow
class DBServiceManagement(IDBServiceManagement):

    def start_service(self,service):
        os.system(f'net start {service}')

    def stop_service(self,service):
        os.system(f'net stop {service}')

    def check_service_is_running(self, service):
        status = subprocess.run(["powershell", "-Command", f'Get-Service -name "{service}"| Format-List -Property Status'], capture_output=True)
        #stat = os.system(f'service {service} status')
        return status