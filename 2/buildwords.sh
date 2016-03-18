#!/bin/bash
grep '<td>.*</td>' |
sed 's/<[^>]*>//g' |
sed "s/\`/\'/g" |
sed "s/\,/ /g" |
tr -s '[:blank:]' '[\n*]' |
tr '[:upper:]' '[:lower:]' |
sed "/[^pkmnwlhaeiou'\'']/d" |
sort -u
