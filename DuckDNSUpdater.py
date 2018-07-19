#! /usr/bin/python3
import logging
import os
import time
import sys
import urllib.request
import urllib.parse

#Settings (Edit THIS!) you can obtain this from you duckdns.org account
TOKEN = ""
DOMAINS = [""]

def updateDuckDNSDomains(domains:list, token:str, ipv4:str="", ipv6:str="", clear:bool=False, num_rounds=3):
    # https://www.duckdns.org/update?domains={YOURVALUE}&token={YOURVALUE}[&ip={YOURVALUE}][&ipv6={YOURVALUE}][&verbose=true][&clear=true]
    # domains - REQUIRED - comma separated list of the subnames you want to update
    # token - REQUIRED - your account token
    # ip - OPTIONAL - if left blank we detect IPv4 addresses, if you want you can supply a valid IPv4 or IPv6 address
    # ipv6 - OPTIONAL - a valid IPv6 address, if you specify this then the autodetection for ip is not used
    # verbose - OPTIONAL - if set to true, you get information back about how the request went
    # clear - OPTIONAL - if set to true, the update will ignore all ip's and clear both your records 
    url = "https://www.duckdns.org/update?" + urllib.parse.urlencode({"domains": ",".join(domains), "token": token, "ip": ipv4, "ipv6": ipv6, "clear": str(clear).lower()})
    for round in range(num_rounds):
        try:
            with urllib.request.urlopen(url) as conn:
                data = conn.read().decode()
            return data == "OK"
        except KeyboardInterrupt:
            break
        except:
            continue
    return False

if __name__ == "__main__":
    if not os.path.exists("./Logs/"):
        os.mkdir("Logs")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s -->> %(message)s",
        handlers=[
            logging.FileHandler("./Logs/{0}.log".format(time.strftime("%Y-%m-%d"))),
            logging.StreamHandler()
        ]
    )
    log = logging.getLogger("DuckDNSUpdater")
    if updateDuckDNSDomains(DOMAINS,TOKEN):
        log.info("Update: OK")
    else:
        log.error("Update: FAIL")

