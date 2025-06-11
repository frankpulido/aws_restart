#!/bin/bash
COUNTER_FILE="myFiles/.counter"
mkdir -p myFiles
if [ -f "$COUNTER_FILE" ]; then
        counter=$(cat "$COUNTER_FILE")
else
        counter=1
fi
end=$((counter+25))
for ((i=$counter; i<end; i++)); do
        touch myFiles/frank_pulido_$i.txt
        echo "File frank_pulido$i.txt has been created"
done
echo "$i" > "$COUNTER_FILE"
