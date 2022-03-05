#!/bin/bash 

#Initial Nmap Scan (flags can be changed based on preference) 
echo 'Initial nmap scan beginning...' 
echo 'Please enter the target IP address:'  
read IP 
#File Path (ex: /home/steven/Documents/htb/filename)
echo 'Please enter your desired file path and filename:' 
read filename 
parent=$(dirname $filename) 
nmap -sC -sV -O $IP -oA $filename  
#All ports scan
echo -e '\nAll ports scan beginning...This may take a while...' 
nmap -p- -sV $IP --max-retries 4 
#UDP scan
echo -e '\nUDP scan beginning...This may take a while...' 
nmap -sV -sU $IP --max-retries 4 

echo -e '\nAll nmap scans complete!'
