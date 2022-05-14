import re
import os
import requests
import platform
import webbrowser
import sys


def dnsmap():
    domain = sys.argv[1]
    os.system("touch a.txt")
    os.system("echo '<br>[+] Gathering information about the DNS servers<br>' >> a.txt")
    os.system("echo '<br>[+] Identifying the MX and TXT records<br>' >> a.txt")
    os.system("echo '<br>[+] DNS Map of the domain created successfully!<br>' >> a.txt") 
    url = "file:///root/Sentry/" + domain[:-4] + ".png"
    response = requests.Session().get('https://dnsdumpster.com/').text
    try: csrf_token = re.search(r"name='csrfmiddlewaretoken' value='(.*?)'", response).group(1)
    except: csrf_token = None

    cookies = {'csrftoken': csrf_token}
    headers = {'Referer': 'https://dnsdumpster.com/'}
    data = {'csrfmiddlewaretoken': csrf_token, 'targetip': domain}
    response = requests.Session().post(
        'https://dnsdumpster.com/', cookies=cookies, data=data, headers=headers)

    image = requests.get('https://dnsdumpster.com/static/map/%s.png' % domain)
    if image.status_code == 200:
        image_name = domain.replace(".com","")
        with open('%s.png' % image_name, 'wb') as f:
            f.write(image.content)
            # print("\n%s.png DNS map image stored to current directory" % image_name)
            
            if (platform.system() != "Windows"):
                webbrowser.open(url)
            else:
                os.startfile('%s.png' % image_name)

dnsmap()
os.system("cat a.txt")
os.system("rm a.txt")