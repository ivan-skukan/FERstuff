logs="$1" 
if [ ! -d "$logs" ]; then
    echo "Directory $logs not found. Check that directory exists and run with './z.sh [directory]'."
    exit 1
fi

if [ $# -ne 1 ]; then
    echo "Usage: ./z.sh [directory]"
    exit 1
fi

#cat $logs/* | cut -f2 -d':' | sort | uniq -c | awk '{print $2, $1}' 
for file in $logs/*; do
    cat $file | cut -f2 -d':' | sort | uniq -c | awk '{print $2, $1}'
done

