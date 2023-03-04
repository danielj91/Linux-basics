#! /bin/bash

nmap -sT 192.168.64.0/24 -p 1433 >/dev/null -oG MSSQLscan
cat MSSQLscan | grep open > MSSQLscan2
cat MSSQLscan2
