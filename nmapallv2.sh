#!/bin/bash 

echo 'Initial nmap scan beginning...' 
echo 'Please enter the target IP address:'  
read IP 
echo 'Please enter your desired file path and filename:' 
read filename 
parent=$(dirname $filename) 
nmap -sC -sV -O $IP -oA $filename  

echo -e '\nAll ports scan beginning...' 
nmap -p- -sV $IP --max-retries 4 

echo -e '\nUDP scan beginning...' 
nmap -sV -sU $IP --max-retries 4 

echo -e '\nAll nmap scans complete!'
