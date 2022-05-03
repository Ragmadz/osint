import re
import smtplib
import dns.resolver
import os
import time
import sys

# Address used for SMTP MAIL FROM command  
fromAddress = 'corn@bt.com'

# Simple Regex for syntax checking
regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

# Email address to verify
inputAddress = sys.argv[1]
addressToVerify = str(inputAddress)

# Syntax check
match = re.match(regex, addressToVerify)
if match == None:
	print('Bad Syntax')
	raise ValueError('Bad Syntax')

# Get domain for DNS lookup
splitAddress = addressToVerify.split('@')
domain = str(splitAddress[1])
os.system("touch a.txt")
urla = "echo '<br>[+] <b><u>Domain</b></u> - '" + domain
urlb = urla + " >> a.txt"
os.system(urlb)
urla = "echo '<br>[+] <b><u>The MX records for the domain name are</b></u> - '"
urlb = urla + " >> a.txt"
os.system(urlb)
os.system("nslookup -q=mx gmail.com | sed '/Server/ d' | sed '/Address/ d' | sed '/answer/ d' >> a.txt")

# MX record lookup
records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)


# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)

# SMTP Conversation
os.system("echo '[+] Establishing an SMTP connection with the server<br>' >> a.txt")
# time.sleep(4)
server.connect(mxRecord)
os.system("echo '[+] Connection with the server established successfully!<br>' >> a.txt")
server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
os.system("echo '[+] Checking the email address<br>' >> a.txt")
# time.sleep(4)
server.mail(fromAddress)
os.system("echo '[+] Sending an SMTP request' >> a.txt")
# time.sleep(4)
code, message = server.rcpt(str(addressToVerify))
server.quit()

#print(code)
#print(message)

# Assume SMTP response 250 is success
if code == 250:
	os.system("echo '<br><b><u>Result</b</u> - The email address is valid' >> a.txt")
else:
	os.system("echo '<br><b><u>Result</b></u> - The email address is not valid' >> a.txt")
with open('a.txt', 'r') as root:
        lines = root.readlines()
        
lines = ["<br>" + line for line in lines]
        
with open('a.txt', 'w') as root:
	root.writelines(lines)
os.system("cat a.txt")
os.system("rm a.txt")