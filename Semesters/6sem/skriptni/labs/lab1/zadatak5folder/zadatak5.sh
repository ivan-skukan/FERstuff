arg="$1"

echo "$0, $1"

count=$(find . -name "*$arg*" -print0 | xargs -0 grep -c . | awk -F: '{sum += $2} END {print sum}')

echo "Number of lines: $count"
:'
while IFS= read -r file
do
  lines=$(wc -l < "$file")
  count=$((count + lines))
done < <(find . -type f -name "*$arg*")
'