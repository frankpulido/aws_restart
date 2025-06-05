# Python 3.9.6
# Author: Frank Pulido
# Date: June 04, 2025
# Purpose: Analyze the insulin sequence
# File: lab12_insulin_net_charge.py
# Encoding: ASCII (a subset of UTF-8)

# Store the human preproinsulin sequence in a variable called preproinsulin
with open("lab10_preproinsulin_seq_cleaned.txt", "r") as file:
    try:
        preproInsulin = file.read().strip()
    except FileNotFoundError:
        print(f"File not found {file}")
        quit()
print("The sequence of human preproinsulin", len(preproInsulin), " : ", preproInsulin)

# Store the remaining sequence elements of human insulin in variables
with open("lab10_aa_lsinsulin_seq_clean.txt", "r") as file:
    try:
        lsInsulin = file.read().strip()
    except FileNotFoundError:
        print(f"File not found {file}")
        quit()
print("The sequence of human ls insulin", len(lsInsulin), " : ", lsInsulin)

with open("lab10_aa_ainsulin_seq_clean.txt", "r") as file:
    try:
        aInsulin = file.read().strip()
    except FileNotFoundError:
        print(f"File not found {file}")
        quit()
print("The sequence of human a insulin", len(aInsulin), " : ", aInsulin)

with open("lab10_aa_binsulin_seq_clean.txt", "r") as file:
    try:
        bInsulin = file.read().strip()
    except FileNotFoundError:
        print(f"File not found {file}")
        quit()
print("The sequence of human b insulin", len(bInsulin), " : ", bInsulin)

with open("lab10_aa_cinsulin_seq_clean.txt", "r") as file:
    try:
        cInsulin = file.read().strip()
    except FileNotFoundError:
        print(f"File not found {file}")
        quit()
print("The sequence of human c insulin", len(cInsulin), " : ", cInsulin)

insulin = bInsulin + aInsulin  # Concatenate b and a chains and convert to lowercase
print()
print("The sequence of human insulin:", len(insulin), " : ", insulin)

pKR = {
    'y': 10.07,  # Tyrosine
    'c': 8.18,   # Cysteine
    'k': 10.53,  # Lysine
    'h': 6.00,   # Histidine
    'r': 12.48,  # Arginine
    'd': 3.65,   # Aspartic acid
    'e': 4.25,   # Glutamic acid
}

seqCount = {aa: insulin.count(aa) for aa in pKR.keys()}
print()
print("Amino acid counts in insulin sequence:", seqCount)

def calculate_net_charge(seqCount, pKR_values, pH):
    net_charge = 0.0
    for aa, count in seqCount.items():
        if aa in ['d', 'e', 'y', 'c']:  # acidic side chains
            net_charge -= count * (1 / (1 + 10**(pH - pKR_values[aa])))
        elif aa in ['k', 'r', 'h']:    # basic side chains
            net_charge += count * (1 / (1 + 10**(pKR_values[aa] - pH)))
    return net_charge

#pH = 7.4  # Physiological pH
pH = 0.0  # Starting pH for the loop
print()
while(pH <= 14):
    net_charge = calculate_net_charge(seqCount, pKR, pH)
    print(f"The net charge of insulin at pH {pH:.1f} is : {net_charge:.2f}")
    pH += 0.1

# The expected net charge of insulin at physiological pH (7.4) is around -2.0
# Note: The actual net charge may vary slightly based on the specific sequence and modifications.
# The program outcome is supposed to be around -2.0, but the actual value may vary slightly based on the specific sequence and modifications.