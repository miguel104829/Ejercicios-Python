import subprocess
import getpass

with open ('E:/copias-SQL/consola/world.sql', 'w') as out:
    subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Server 8.0/bin/mysqldump" --user=root --password={getpass.getpass()} --databases world', stdout=out, shell=True)