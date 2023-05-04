#!/bin/bash
#automated script to run aureport commands into a report

#this section is to help grab reports from the date range you wish and create the name for the report
echo "What is the starting date of the report? (Format MM/DD/YYYY)" 
read start
echo "What is the end date of the report? (Format MM/DD/YYYY)" 
read end
echo "What is the date range of the report? (Format 2023MMDD-2023MMDD)"
read range
echo "What is the hostname of the system you are running this report on? (Format DESKTOP-P1234)" 
read name

###this section will require some updating - edit USER to your username on the system you will be saving the report to (ex: bobjenkins) 
###create a Audits directory on the desktop where the reports will be saved to
aureport -x --summary --start $start --end $end >> /home/USER/Desktop/Audits/$name-$range.txt
aureport --failed -l --start $start --end $end >> /home/USER/Desktop/Audits/$name-$range.txt
aureport --login --summary -i --start $start --end $end >> /home/USER/Desktop/Audits/$name-$range.txt
aureport -au --start $start --end $end >> /home/USER/Desktop/Audits/$name-$range.txt
aureport -m --start $start --end $end >> /home/USER/Desktop/Audits/$name-$range.txt
aureport -t --start $start --end $end >> /home/USER/Desktop/Audits/$name-$range.txt
aureport -f --start $start --end $end >> /home/USER/Desktop/Audits/$name-$range.txt

chmod 744 /home/USER/Desktop/Audits/$name-$range.txt

#this section notifies you the reports are done and will exit after 1 second. 
echo "Aureport has finished generating your audit report. Please see the ~/Audits directory." 
sleep 1
echo "Goodbye."

bash -c "exit"

