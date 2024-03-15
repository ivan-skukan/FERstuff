dir1="$1"
dir2="$2"

for file1 in "$dir1"/*; do
    for file2 in "$dir2"/*; do
        if [ "$(basename "$file1")" = "$(basename "$file2")" ]; then
            if [ "$file1" -nt "$file2" ]; then
                echo "$file1 --> $dir2"  #navodno printa cijeli path
            else
                echo "$file2 --> $dir1"
            fi
        fi
    done
done