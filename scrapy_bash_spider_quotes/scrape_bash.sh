#!/usr/bin/env bash
#web scraping quotes website
 
if [ $# -ne 1 ]; then
	echo "usage $(basename $0) 'page number please'"
	exit -1

fi

curl=$(which curl)
outfile="output.html"
#name=$(echo $1 | tr ' ' '+')
regex="--$1  "
url="https://quotes.toscrape.com/page/$1/"

function dump_webpage(){
	curl -o $outfile $url
	check_errors
}


#clean the webpage
function strip_html(){
	grep "<span>" $outfile > temp.txt && cp temp.txt $outfile
}

 #checking for errors
function check_errors(){
  	[ $? -ne 0 ] && echo "Error downloading page ..." && exit -1
}



#######################
#      MAIN           #
#######################

dump_webpage

#print_quotes
exit -1


