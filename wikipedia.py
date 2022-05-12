import requests
import xmltodict
import json
import ast
import sys
import os

ipuser = sys.argv[1]
# print("\n")
response = requests.get("https://en.wikipedia.org/w/api.php?action=feedcontributions&user=" + ipuser)
parsedata = xmltodict.parse(response.text)
json = json.dumps(parsedata)
a = ast.literal_eval(json)
# print("Title - " + a['rss']['channel']['title'].replace("- ",""))
# print("Link - " + a['rss']['channel']['link'])
# print("Description - " + a['rss']['channel']['description'])
# print("Language - " + a['rss']['channel']['language'])
# print("Generator - " + a['rss']['channel']['generator'])
# print("Build Date - " + a['rss']['channel']['lastBuildDate'])
os.system("touch a.txt")
s = "<br>[+] <b><u>Title</b></u> - " + a['rss']['channel']['title'].replace("- ","")
e = "<br><br>[+] <b><u>Link</b></u> - <a href = '" + a['rss']['channel']['link'] + "'>" + a['rss']['channel']['link'] + "</a>"
n = "<br><br>[+] <b><u>Description</b></u> - " + a['rss']['channel']['description']
t = "<br><br>[+] <b><u>Language</b></u> - " + a['rss']['channel']['language']
r = "<br><br>[+] <b><u>Generator</b></u> - " + a['rss']['channel']['generator']
y = "<br><br>[+] <b><u>Build Date</b></u> - " + a['rss']['channel']['lastBuildDate']
os.system("touch a.txt")
with open ('a.txt', 'w') as root:
	root.writelines(s)
	root.writelines(e)
	root.writelines(n)
	root.writelines(t)
	root.writelines(r)
	root.writelines(y)
os.system("cat a.txt")
os.system("rm a.txt")