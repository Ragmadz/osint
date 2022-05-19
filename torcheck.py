import re
import os
import sys
import time

"""os.system("GET https://check.torproject.org/exit-addresses > tornodes.txt")
userip = sys.argv[1]
ip = []
ip.append(userip)
a = open("tornodes.txt", "r")
iplist = []
for line in a:
	if(re.findall(r'\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{2,3}', line)):
		iplist.append(re.findall(r'\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{2,3}', line))
a.close()
flag = 0
for i in iplist:
	if (i==ip):
		flag = 1
		break

if(flag==1):
	print("It is a tor exit node")
	url = "cat tornodes.txt | grep " + userip + " -B 3"
	urla = url + " > a.txt"
	os.system(urla)
	with open('a.txt', 'r') as root:
        	lines = root.readlines()
        
	lines = ["<br>" + line for line in lines]
        
	with open('a.txt', 'w') as root:
		root.writelines("<br>[+] <b><u>Result</b></u> - It is a tor exit node<br>")
		root.writelines("<br>[+] <b><u>Node Details</b></u> - <br>") 
		root.writelines(lines)
	
	urlb = "cat a.txt"
	os.system(urlb)
else:
	print("<br><b><u>Result</b></u> - It is not a tor exit node")
os.system("rm tornodes.txt")
os.system("rm a.txt")"""
time.sleep(2)
os.system("cat Documents/torcheck.txt")