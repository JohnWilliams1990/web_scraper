#!/bin/bash
#  John Williams
#  105201054
#  Date: Thu. Oct. 4, 2018
#  Program: conf.sh

pip3 install requests
pip3 install bs4

ifdown eth0
ifup eth0
service apache2 restart

