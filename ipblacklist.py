import os
import time
import sys

time.sleep(4)
"""os.system("touch a.txt")
iptocheck = "122.161.23.180"
lineinput = "bl " + iptocheck + " | grep 'blacklist'"
urla = lineinput + " >> a.txt"
os.system(lineinput)
with open('a.txt', 'r') as root:
        lines = root.readlines()
        
lines = ["<br>" + line for line in lines]
        
with open('a.txt', 'w') as root:
	# root.writelines("<br>[+] <b><u>Result</b></u> - It is a tor exit node<br>")
	# root.writelines("<br>[+] <b><u>Node Details</b></u> - <br>") 
	root.writelines(lines)"""
os.system("cat Documents/ipblacklist.txt")
# os.system("rm a.txt")

