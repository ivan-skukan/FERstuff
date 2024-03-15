#zadatak 2
echo "$(grep -E -i "banana|jabuka|lubenica|dinja|jagoda" namirnice.txt)"
echo #newline
echo "$(grep -E -i -v "banana|jabuka|lubenica|dinja|jagoda" namirnice.txt)"
echo
echo "$(grep -H -E -r ' *[[:upper:]]{3}[[:digit:]]{6} *' ~/projekti/)" 
echo
echo "$(find -type f -mtime +7 -mtime -14 | ls)" #dovrsi
echo
for i in $(seq 1 15); do echo $i; done

kraj=15
for i in $(seq 1 15); do echo $i; done #nekaj sa sekvencama dovrsi
for ((i=1; i<=$kraj; i++)); do echo $i; done
