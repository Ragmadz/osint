import requests
import time
import sys

email = sys.argv[1]
url = "https://psbdmp.cc/api/search/email/" + email
response = requests.get(url)
print("[+] Searching leaks on pastebin<br>")
time.sleep(4)
if(response.json()['count'] == 0):
	print("<br>[+] <b><u>No leaks on pastebin</b></u><br>")
else:
	print("<br>[+] <b><u>Leak count on pastebin</b></u> - " + str(response.json()['count']))
	print("<br>")
	for i in range(response.json()['count']):
		a = {}
		leakcount = i + 1
		a = response.json()['data']
		date, time = a[i]['time'].split(" ")
		print("<br>[+] <b><u>Leak " + str(leakcount) + "</b></u>")
		print("<br>Pastebin Link - <a href = 'https://pastebin.com/" + a[i]['id'] + "'>" + "https://pastebin.com/" + a[i]['id'] + "</a>")
		print("<br>Leak Date - " + date)
		print("<br>Leak Time - " + time)
		print("<br>")