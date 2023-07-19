#https://learn.microsoft.com/de-de/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3
#Es wurde mit Set-Executionpolicy von restricted auf unrestricted gestellt
#Es wurde mit Set-ExecutionPolicy auf RemoteSigned gestellt
Get-Service -name "MySQL80"| Format-List -Property Status