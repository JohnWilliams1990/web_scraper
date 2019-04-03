#!/bin/bash
#  John Williams
#  105201054
#  Date: Wed. Aug. 29, 2018
#  Program: enum.sh


##########################################################
#folder='newFolder'
#http='http://www.yahoo.com/'
##http='http://zonetransfer.me/'
##http='https://www.dairyqueen.com/us-en/?localechange=1&'
##http='http://www.stealmylogin.com'
#rm -rf $folder
#skipfish -o $folder $http
#
##sleep 10 
#cd $folder
#firefox index.html 
#
##########################################################


#dnsenum  -o mydomain.xml google.com 
#dnsenum  google.com 
#dnswalk zonetransfer.me.

#dnsenum  zonetransfer.me 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#dnsenum  zonetransfer.me | grep -B 8 'Trying Zone Transfers and getting Bind Versions'
#
#for i in `dnsenum  zonetransfer.me | grep -B 8 'Trying Zone Transfers and getting Bind Versions' | grep -v "getting" | awk '{print $5}'` ; do 
#echo '~~~~~~~~~~~'
#
#echo $i
##dnsdict6 $i
#
#done
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#dnsdict6 google.com

#for i in `dnsdict6 google.com` ; do 
#
#echo $i 
#value=$(echo $i | awk '{print $3}')
#echo $value
##address6 $value
#done

#########################################################
#The above technique might trigger Google's Bot detection after too many requests.
# may work for a while until dns server says your botting
#https://tools.kali.org/information-gathering/goofile
#goofile -d scp.nrc.gov -f pdf 
#goofile -d google.com -f pdf 
#goofile -d ucdenver.edu -f pdf
goofile -d zonetransfer.me -f pdf
#goofile -d msudenver.edu -f pdf 
#########################################################


#~~~~~~~> probably not going to use
#https://digi.ninja/projects/zonetransferme.php
#dnswalk zonetransfer.me.
