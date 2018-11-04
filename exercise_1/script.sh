#!/bin/bash
# Check for existence of params
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Please enter the URL and the search term."
    exit 1
fi

# Print occurences of word in website to stdout
wget -q -O - $1 | grep -o $2

# Fetch urls from website
# tr converts single quotes to double quotes for simpler regex
# only get hrefs inside <a>
urls=$(wget -q -O - $1 | \
       tr "'" '"' | \
       grep -Po '(?i)<a([^>]+)>(.+?)</a>' | \
       grep -Po '(?<=href=")[^"]*(?=")')

for url in $urls; do
    if [ $url != $1 ]; then
        ./script.sh $url $2
    fi
done