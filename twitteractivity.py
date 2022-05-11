import os
import time
import sys

time.sleep(4)
"""username = sys.argv[1]
username = str(username)
os.system("touch a.txt")
urla = "python tweets_analyzer.py -n " + username
urlb = urla + " >> a.txt"
os.system(urlb)
with open('a.txt', 'r') as root:
        lines = root.readlines()
        
lines = ["<br>" + line for line in lines]
        
with open('a.txt', 'w') as root:
	root.writelines(lines)"""
os.system("cat Documents/twitter.txt")
# os.system("rm a.txt")