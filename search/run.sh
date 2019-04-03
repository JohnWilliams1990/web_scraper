#!/bin/bash
#  John Williams
#  105201054
#  Date: Wed. Mar. 20, 2019
#  Program: run.sh

read -p "Search phrase:" input 
echo $input

#declare iterations=5
declare iterations=10
# input=`echo $input | sed "s/ /%20/g"`
input=`echo $input | sed "s/ /+/g"`
echo $input



#./d33p.sh -l 10 -b stuxnet | grep http
 websites=`./d33p.sh -l $iterations -b $input | grep http | sed "s/:\-/ /g" | awk '{print $2}'`

declare -A hash
for i in ${websites[@]} ; do 
  hash[$i]=$i
done

for k in "${!hash[@]}"
do
    echo "$k"
done

echo
echo

rm -rf files
mkdir files
cd files
for i in ${websites[@]} ; do 
  echo $i | grep -v "\.\.\." #| grep -v "youtube"

  wget \
    --reject js,css,ico,txt,gif,jpg,jpeg,png,mp3,pdf,tgz,flv,avi,mpeg,iso \
    --html-extension \
    --quiet \
    --limit-rate=200k \
    --no-clobber \
    --random-wait \
    --cut-dirs=3 \
    -nd \
    -e robots=off \
    --show-progress $i

    #--output-document=stuff.txt \
    #--level=2 \
    #-r -E -e \
    #-r -E -e \
   # --convert-links \ 

    # --no-clobber \
# --ignore-tags=img,link,script \
#--header="Accept: text/html"

    # --page-requisites \
    # --html-extension \


done 


