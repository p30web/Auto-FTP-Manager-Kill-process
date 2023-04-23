import psutil
import subprocess

for proc in psutil.process_iter():
    try:

        pinfo = proc.as_dict(attrs=['pid', 'name'])

        if 'Auto FTP Manage' in pinfo['name']:
            proc.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

subprocess.Popen("C:\Program Files (x86)\Deskshare\Auto FTP Manager 7/Auto FTP Manager.exe")