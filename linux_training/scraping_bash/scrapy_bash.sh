grep 2 index.txt | grep '>[0-9]' |  sed 's/a\> /\n/g' | cut -d'>' -f2 | cut -d'<' -f1
