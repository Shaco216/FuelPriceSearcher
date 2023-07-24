#https://stackoverflow.com/questions/46595845/python-command-to-stop-and-start-windows-services
import os
import subprocess, sys
from IDBServiceManagement import IDBServiceManagement
#windows service running check
#https://stackoverflow.com/questions/46579170/python-code-to-check-if-service-is-running-or-not

#todo: https://stackoverflow.com/questions/21944895/running-powershell-script-within-python-script-how-to-make-python-print-the-pow

#check service: https://www.youtube.com/watch?v=LvGqh7IeVkI
class DBServiceManagement(IDBServiceManagement):

    def start_service(self,service):
        os.system(f'net start {service}')

    def stop_service(self,service):
        os.system(f'net stop {service}')

    def check_service_is_running(self):
        #https://stackoverflow.com/questions/21944895/running-powershell-script-within-python-script-how-to-make-python-print-the-pow
        p = subprocess.Popen(["powershell.exe",
                              "Get-Service -name 'MySQL80'| Format-List -Property Status"],stdout=subprocess.PIPE)
        status = False
        out, err = p.communicate()
        out = str(out)
        firstStringRemove= str("b'\\r\\n\\r\\nStatus : ")
        secondStringRemove = str("\\r\\n\\r\\n\\r\\n\\r\\n'")
        try:
            out = out.replace(firstStringRemove,"")
            out = out.replace(secondStringRemove,"")
        except Exception as e:
            print("Fehler beim Replacen genauer: " + str(e))
        #print(out)
        status = out
        return status

        #command = subprocess.run(["powershell", "-Command", f'Get-Service -name "{service}"| Format-List -Property Status'], capture_output=True)
        #status = command.stdout.decode('utf-8')
        #print(status)
        #stat = os.system(f'service {service} status')
        #return status