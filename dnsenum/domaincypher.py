import sys

from funci import *
try:
    module = sys.argv[1]

    if module:
        if module == '1':
            domain = sys.argv[2]
            dnsenum(domain)
        elif module == '2':
            domain = sys.argv[2]
            wordlist = sys.argv[3]
            subdomain(domain, wordlist)
        elif module == 3:
            print("Open a listener ")
        elif module == '4':
            domain = sys.argv[2]
            testWHois(domain)

except:
    try:
        with open('ascii-art.txt', 'r') as asciiFile:
            newFile = asciiFile.read()
            print(newFile)
            print("This tools is only study purpose, everything here is for improve my self\n"
                  "I gonna use that tool for some simple enumerations in websites, reverse shell etc.")
            print("usage: python3 dnscypher <option> <website> <wordlist>")
    except Exception as error:
        print(error)

    print("1 - DnsEnum\n"
           "2 - Subdomain Enum\n"
           "3 - Listener with netCat\n"
           "4 - Whois Domain\n"
           "5 - Nmap Default scanning\n"
           "6 - Nmap Stealth scanning")
