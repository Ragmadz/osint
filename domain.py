from requests import get
import os
import sys

domain = sys.argv[1]
urla = "whois " + domain + " | sed -n '/The Registry/,/>>>/p'" + " | sed '/The Registry/d'" + " | sed '/Ext/d'" + " | sed '/>>>/d'" + " | sed '/Fax/d'" + " | sed '/Reporting/d'" + " | sed '/Registrars./d'"
urlb = urla + " > a.txt" 
os.system(urlb)
with open('a.txt', 'r') as root:
        lines = root.readlines()
        
lines = ["<br>" + line for line in lines]
        
with open('a.txt', 'w') as root:
	root.writelines(lines)
	
os.system("cat a.txt")
os.system("rm a.txt")