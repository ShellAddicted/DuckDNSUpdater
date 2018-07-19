# DuckDNSUpdater
A Python way to update duckdns.org records

## Usage (cron)
```bash
$ git clone https://github.com/ShellAddicted/DuckDNSUpdater
$ crontab -e
```
and add the following line: (<b>replace the script path with its actual location</b>)

```
*/15 * * * * python3 /home/shelladdicted/DuckDNSUpdater/DuckDNSUpdater.py
```
