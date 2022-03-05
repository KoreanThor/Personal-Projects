#!/bin/bash 

echo 'Initial nmap scan beginning...' 
echo 'Please enter the target IP address:'  
read IP 
nmap -sC -sV -O $IP 

echo -e '\nAll ports scan beginning...' 
nmap -p- -sV $IP --max-retries 4 

echo -e '\nUDP scan beginning...' 
nmap -sV -sU $IP --max-retries 4 

echo -e '\nAll nmap scans complete!' 
