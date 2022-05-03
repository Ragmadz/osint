import requests
import sys
import os

os.system("touch a.txt")
name, comp = sys.argv[1].split(",")
namea, nameb = name.split(" ")
if(".com" in comp):
	response = requests.get("https://api.hunter.io/v2/email-finder?domain=" + comp + "&first_name=" + namea + "&last_name=" + nameb + 	  	  "&api_key=9dc2c29d48572d5f63c0f81ff0fd076cd5b2d321")
else:
	response = requests.get("https://api.hunter.io/v2/email-finder?company=" + comp + "&full_name=" + namea + "+" + nameb + "&api_key=9dc2c29d48572d5f63c0f81ff0fd076cd5b2d321")
a = response.json()
p = "<br>[+] <b><u>Name</b></u> - " + namea + " " + nameb + "<br>"
q = "<br>[+] <b><u>Company</b></u> - " + a['data']['company'] + "<br>"
r = "<br>[+] <b><u>Domain</b></u> - " + a['data']['domain'] + "<br>"
s = "<br>[+] <b><u>Email</b></u> - " + a['data']['email'] + "<br>"
with open ('a.txt', 'w') as root:
	root.writelines(p)
	root.writelines(q)
	root.writelines(r)
	root.writelines(s)
os.system("cat a.txt")
os.system("rm a.txt")


