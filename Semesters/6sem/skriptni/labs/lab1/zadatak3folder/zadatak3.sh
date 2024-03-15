#test
#-d: ispis ponovljenih redaka, -c: broj ponavljanja
#sort <file> | uniq?

directory="$1"

for log in "$directory"/*; do
	firstline=$(head -n 1 "$log")
	datum=$(echo "$firstline" | grep -oE '[0-9]{2}/[[:alpha:]]{3}/[0-9]{4}')
	echo "datum: $datum"
	echo "======================================================="
	grep '"GET\|POST' "$log" | sed 's/^.*"\(GET\|POST\) \([^"]*\)".*$/\1 \2/' | sort | uniq -c | sort -nr
done


