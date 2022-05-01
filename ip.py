from requests import get
import os
import sys

ip = sys.argv[1]
url = "whois " + ip + " > a.txt" 
os.system(url)
with open('a.txt', 'r') as root:
        lines = root.readlines()
        
lines = ["<br>" + line for line in lines]
        
with open('a.txt', 'w') as root:
	root.writelines(lines)
	
os.system("cat a.txt")
os.system("rm a.txt")
# os.system("GET whois.com/whois/ip | sed -n '/inetnum:/,/% This/p'")
# url = "GET https://whois.com/whois/" + ip + " | sed -n '/inetnum:/,/% This/p'" + " | sed '/^remarks/ d'" + " | sed '/email/ d'" 
