# Python 3.9.6
# Author: Frank Pulido
# Date: June 04, 2025
# Purpose: Analyze the insulin sequence
# File: lab11_analyze_insulin.py
# Encoding: ASCII (a subset of UTF-8)

# Store the human preproinsulin sequence in a variable called preproinsulin
with open("lab10_preproinsulin_seq_cleaned.txt", "r") as file:
    preproInsulin = file.read().strip()

# Store the remaining sequence elements of human insulin in variables
with open("lab10_aa_lsinsulin_seq_clean.txt", "r") as file:
    lsInsulin = file.read().strip()

with open("lab10_aa_ainsulin_seq_clean.txt", "r") as file:
    aInsulin = file.read().strip()

with open("lab10_aa_binsulin_seq_clean.txt", "r") as file:
    bInsulin = file.read().strip()

with open("lab10_aa_cinsulin_seq_clean.txt", "r") as file:
    cInsulin = file.read().strip()


# Printing "the sequence of human insulin" to console using successive print() commands
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner)
print("The sequence of human insulin, chain a:", aInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

insulin = bInsulin + aInsulin

# Count the number of each amino acids
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})

# Calculate the molecular weight of insulin
molecularWeightInsulin = sum([aaWeights[aa] * aaCountInsulin[aa] for aa in aaCountInsulin])
# Print the molecular weight of insulin
print("The rough molecular weight of human insulin is: {:.2f} Da".format(molecularWeightInsulin))

# The program outcome is supposed to be 6696.42 Da, but the actual value is 5807.63 Da
molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))