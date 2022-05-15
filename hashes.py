import requests
import sys
import os

string = sys.argv[1]
response = requests.get("https://hashes.org/api.php?key=BasyqoIBm5GKPfsq1usCQNXXOLSGcg&query=" + string)
Plaintext = response.json()["result"][string]["plain"] 
Algorithm = response.json()["result"][string]["algorithm"]
# print("Plaintext = ", Plaintext)
# print("Algorithm = ", Algorithm)
os.system("touch a.txt")
a = "<br>[+] <b><u>Plaintext</b></u> - " + Plaintext
b = "<br><br>[+] <b><u>Algorithm</b></u> - " + Algorithm
with open ('a.txt', 'w') as root:
	root.writelines(a)
	root.writelines(b)
os.system("cat a.txt")
os.system("rm a.txt") 





