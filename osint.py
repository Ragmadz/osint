import os

def banner():
	return("""
								 ____             _              
								/ ___|  ___ _ __ | |_ _ __ _   _ 
								\___ \ / _ \ '_ \| __| '__| | | |
								 ___) |  __/ | | | |_| |  | |_| |
								|____/ \___|_| |_|\__|_|   \__, |
											   |___/ 		                                              
""")

os.system("clear")
print(banner())

def prRed(skk): print("\033[91m{}\033[00m".format(skk)) 
def prGreen(skk): print("\033[92m{}\033[00m".format(skk)) 
def prYellow(skk): print("\033[93m{}\033[00m".format(skk)) 
def prPurple(skk): print("\033[95m{}\033[00m".format(skk)) 
def prCyan(skk): print("\033[96m{}\033[00m".format(skk)) 

prGreen("                                                      Developers - Raaghav Mathur, Anuj Arora and Anshu Meena")
prYellow("\nSentry is an open source intelligence (OSINT) automation tool. It integrates multiple data sources that are available publicly and utilises a range of methods for    data analysis, making it easy to navigate through data and create reports.\n")
prCyan("FEATURES\n")
prCyan("1. Enumerate information about an IP address")
prCyan("2. Check if an IP address is blacklisted")
prCyan("3. Check if an IP address is that of a tor exit node")
prCyan("4. Check a username on multiple social media websites")
prCyan("5. Analyse user activity on Twitter")
prCyan("6. Analyse edits on Wikipedia pages made by a user")    
prCyan("7. Gather email addresses related to a given domain name")
prCyan("8. Gather basic information about a domain name")
prCyan("9. Gather detailed information about a domain name")
prCyan("10. Create a DNS map for the domain name")
prCyan("11. Crack hashes related to multiple algorithms")
prCyan("12. Check the validity of an email address")
prCyan("13. Check if an email address has been compromised")
prCyan("14. Check if an email address was leaked on pastebin")
prCyan("15. Discover hosts and services on a network")
prCyan("16. Check if it's a honeypot or a real system")
prCyan("17. Check if a file is infected with a malware")
prCyan("18. Update Sentry to it's latest version")

user_input = int(input("\nChoose an option \n"))

if(user_input==1):
	os.system("python3 ip.py")

if(user_input==2):
	iptocheck = input("Enter an IP address \n")
	lineinput = "bl " + iptocheck
	os.system(lineinput)

if(user_input==3):
	os.system("python3 torcheck.py")

if(user_input==4):
	username = input("Enter a valid username \n")
	line = "python3 username.py " + username + " | grep " + username
	os.system(line)

if(user_input==5):
	handle = input("Enter username \n")
	sentence = "python tweets_analyzer.py -n " + handle
	os.system(sentence)

if(user_input==6):
	os.system("python3 wikipedia.py")

if(user_input==7):
	domain = input("Enter the domain name \n")
	statement = "theHarvester -d " + domain + " -b all " + "| sed -n '/Target/,//p'"
	os.system(statement)

if(user_input==8):
	os.system("python3 domain.py")

if(user_input==9):
	domain = input("Enter a domain name \n")
	url = "domain_analyzer.py -d " + domain
	os.system(url)

if(user_input==10):
	os.system("python3 domainimage.py")

if(user_input==11):
	os.system("python3 hashes.py")

if(user_input==12):
	os.system("python3 emailaddress.py")

if(user_input==13):
	os.system("python3 emailleak.py | awk '{$1=$1};1'")

if(user_input==14):
	os.system("python3 pastebin.py") 
