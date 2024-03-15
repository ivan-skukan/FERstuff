direktorij="$1"

if [ ! -d "$direktorij" ]; then
	echo "Check that the directory exists then pass it as an argument."
	exit 1
fi

cd "$direktorij"

declare -A photos #potrebno za dobar ispis datuma????
#pwd

for img in *; do
	date=$(echo "$img" | cut -c1-6)
	date=${date:0:4}-${date:4:2}
	#date+="-$(echo "$img" | cut -c5-6)" #ista stvar
	photos["$date"]+="$img\n"
	#echo "$date"
done

for date in "${!photos[@]}"; do
	echo -e "$date"
	echo -e "${photos[$date]}" | sort | cat -n
	echo "--------------Ukupno: $(echo -e "${photos[$date]}" | wc -l) fotografija--------------"
done

: '
comment
'
#todo: poredat po mjesecima, rijesit problem prve linije