name=$(sort -R /usr/share/dict/american-english | awk 'NR <= 1 { print $1 }') && echo $name
