#!/bin/bash

# Input file to clean
INPUT="lab10_preproinsulin_seq.txt"

# Output cleaned file (created when the script is run)
OUTPUT="lab10_preproinsulin_seq_cleaned.txt"

# Clean, remove empty lines, and join into one line
sed 's/ORIGIN//g' "$INPUT" | \
  sed 's/[^a-z]//g' | \
  sed '/^$/d' | \
  tr -d '\n' > "$OUTPUT"

wc -m "$OUTPUT"
echo "Cleaning complete. Output saved to $OUTPUT"

# In lsinsulin-seq-clean.txt, save characters 1 to 24. Verify that your file has 24 characters.
# In binsulin-seq-clean.txt, save characters 25 to 54. Verify that your file has 30 characters.
# In cinsulin-seq-clean.txt, save characters 55 to 89. Verify that your file has 35 characters.
# In ainsulin-seq-clean.txt, save characters 90 to 110. Verify that your file has 21 characters.

# Split the cleaned file into specified segments
OUTPUT_NO_NEWLINE=$(mktemp)
tr -d '\n' < "$OUTPUT" > "$OUTPUT_NO_NEWLINE"

head -c 24 "$OUTPUT_NO_NEWLINE" > lab10_aa_lsinsulin_seq_clean.txt
tail -c +25 "$OUTPUT_NO_NEWLINE" | head -c 30 > lab10_aa_binsulin_seq_clean.txt
tail -c +55 "$OUTPUT_NO_NEWLINE" | head -c 35 > lab10_aa_cinsulin_seq_clean.txt
tail -c +90 "$OUTPUT_NO_NEWLINE" | head -c 21 > lab10_aa_ainsulin_seq_clean.txt

rm "$OUTPUT_NO_NEWLINE"

wc -m lab10_aa_lsinsulin_seq_clean.txt
wc -m lab10_aa_binsulin_seq_clean.txt
wc -m lab10_aa_cinsulin_seq_clean.txt
wc -m lab10_aa_ainsulin_seq_clean.txt