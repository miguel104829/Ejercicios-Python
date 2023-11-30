import subprocess
import getpass

subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql" --user=root --password={getpass.getpass()} < E:/copias-SQL/consola/world.sql', shell=True)