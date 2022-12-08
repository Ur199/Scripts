import os
from datetime import date
os.system("git clone https://github.com/hothaifa96/DevSecOps11.git /home/uri/Desktop/Script1")
FileName = "GitBackup"
today = date.today()
FileName = FileName + today
os.system ('mv DevSecOps11 test' + FileName)