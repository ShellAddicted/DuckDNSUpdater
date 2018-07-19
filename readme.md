# DuckDNSUpdater
A Python way to update duckdns.org records

## Usage (cron)
```bash
$ git clone https://github.com/ShellAddicted/DuckDNSUpdater
```
Set `DOMAINS` and `TOKEN` variables of `DuckDNSUpdater.py` lines: 10-12 with your own values:  
Example:
```python
TOKEN = "2983a851-8e8d-48a4-9c93-0d1a276fadcb"
DOMAINS = ["myawesomesubdomain"] #myawesomesubdomain.duckdns.org
```
then `$crontab -e` and add the following line: (<b>replace the path with DuckDNSUpdater actual location</b>)
```
*/15 * * * * python3 /home/shelladdicted/DuckDNSUpdater/DuckDNSUpdater.py
```
