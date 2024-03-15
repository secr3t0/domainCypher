import subprocess

from dns import *
from whois import *


def dnsenum(domain):
    dns_resolver = resolver.resolve(domain, "A")
    for dns in dns_resolver:
        return print("{}, {}".format(domain, dns))


def subdomain(domain, wordlists):
    try:
        with open(wordlists, 'r') as file:
                subdomains = file.read().splitlines()
                for sub in subdomains:
                    dominio = "{}.{}".format(sub, domain)
                    try:
                        result = resolver.resolve(dominio, "A")
                        for dns in result:
                            print("{}, {}".format(dominio, dns))
                    except:
                       pass
    except:
        print("error no arquivo")


def testWHois(domain):
    try:
        result = whois(domain)
        print(result)
    except:
        print("Algum erro aconteceu")


def nmapCommom(domain):
    command = 'ping {}'.format(domain)