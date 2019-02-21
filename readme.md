# DuckDNSUpdater
A Python (unofficial) way to update www.duckdns.org records

## Disclaimer
I'm not affiliated in any way with www.duckdns.org.  
I just use their awesome service.

## Setup
Create an account on www.duckdns.org, create one (or more) subdomain(s) and get your `TOKEN`.
```bash
$ git clone https://github.com/ShellAddicted/DuckDNSUpdater
$ cd DuckDNSUpdater
$ nano DuckDNSUpdaterSettings.json
```
Fill `SubDomains` and `Token` with your own values:  
Example:
```json
{
  "DuckDNS.org": {
    "Token": "2983a851-8e8d-48a4-9c93-0d1a276fadcb",
    "SubDomains": [
      "myawesomesubdomain",
      "anothersubdomain"
    ]
  },
  "LogPath": "./DuckDNSUpdaterLogs/"
}
```

## Usage (manual)
just run it.
```bash
$ python3 ./DuckDNSUpdater.py
```
## Usage (cron)
to continuously update your records  
run `$ crontab -e` and add the following line:  
(<b>remember to set the correct the path</b>)
```
*/15 * * * * python3 /home/shelladdicted/DuckDNSUpdater/DuckDNSUpdater.py
```
