#! /usr/bin/python3
import logging
import os
import sys
import time
import urllib.request
import urllib.parse


def updateDuckDNSDomains(domains: list, token: str, ipv4: str = "", ipv6: str = "", clear: bool = False, attempts=3):
    """
    Perform a HTTP GET request to www.duckdns.org, updating your subdomain(s) records

    :param domains: (required) list of the subdomains you want to update
    :param token: (required) your DuckDNS account token
    :param ipv4: (optional) a valid IPv4, if left blank ("") IPv4 addresses will be auto-detected.
    :param ipv6: (optional) a valid IPv6 address, IPv6 auto-detection may not work check out DuckDNS.org for more info.
    :param clear: (optional) if true, IPv4 and IPv6 will be ignore and all records will be cleared.
    :param attempts: max number of attempts if request fails
    :rtype: boolean
    :return: (bool) Status (True = Success)
    """
    # Dev Note: GET to https://www.duckdns.org/update
    # urlencoded params:
    # domains={YOURVALUE}&token = {YOURVALUE}[&ip={YOURVALUE}][&ipv6 = {YOURVALUE}][ & verbose = true][ & clear = true]
    url = "https://www.duckdns.org/update?" + urllib.parse.urlencode({"domains": ",".join(domains), "token": token,
                                                                      "ip": ipv4, "ipv6": ipv6,
                                                                      "clear": str(clear).lower()
                                                                      })
    for i in range(attempts):
        try:
            with urllib.request.urlopen(url) as conn:
                data = conn.read().decode()
            return data == "OK"
        except KeyboardInterrupt:
            break
        except Exception:
            continue
    return False


def main(cfgPath: str = "./DuckDNSUpdaterSettings.json"):
    import json
    with open(cfgPath, "r") as f:
        cfg = json.load(f)

    state = updateDuckDNSDomains(cfg["DuckDNS.org"]["SubDomains"], cfg["DuckDNS.org"]["Token"])
    if cfg["LogPath"] is not None:
        if not os.path.exists(cfg["LogPath"]):
            os.mkdir(cfg["LogPath"])

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s -->> %(message)s",
            handlers=[
                logging.FileHandler(os.path.join(cfg["LogPath"], time.strftime("%Y-%m-%d.log"))),
                logging.StreamHandler()
            ]
        )
        log = logging.getLogger("DuckDNSUpdater")
        log.info("Update: OK" if state else "Update: FAIL")
    sys.exit(not state)


if __name__ == "__main__":
    main()
