# Python 3.9.6
# Author: Frank Pulido
# Date: June 04, 2025
# Purpose: Calculates the molecular weight of human insulin
# File: lab11_analyze_insulin.py
# Encoding: ASCII (a subset of UTF-8)

# This script calculates the molecular weight of human insulin
from datetime import datetime
updated = datetime(2025, 6, 5)

import lab14_jsonFileHandler

insulin_data = lab14_jsonFileHandler.readJsonFile("lab14_insulin_data.json")

print()
print("This script calculates the molecular weight of human insulin")

if len(insulin_data) > 0:
    binsuline = insulin_data["molecules"]["bInsulin"]
    ainsulin = insulin_data["molecules"]["aInsulin"]
    insulin = (binsuline + ainsulin).upper()
    molecularWeightInsulinActual = insulin_data['molecularWeightInsulinActual']
    print("bsinsulin sequence [",len(binsuline),"] : ", binsuline)
    print("ainsulin sequence [",len(ainsulin),"] : ", ainsulin)
    print("The sequence of human insulin [", len(insulin), "] : ", insulin)
    print("The rough molecular weight of human insulin is: {:.2f} Da".format(molecularWeightInsulinActual))
else:
    print("No data found in the JSON file. Please check the file path and content.")
    quit()

# Calculating the molecular weight of insulin  
# Getting a list of the amino acid (AA) weights  
aaWeights = insulin_data['weights']

seqCount = {aa: insulin.count(aa) for aa in aaWeights.keys()}
print()
print("Amino acid counts in insulin sequence:", seqCount)

molecularWeightInsulin = sum([aaWeights[aa] * seqCount[aa] for aa in seqCount])
# Print the molecular weight of insulin
print("The calculated rough molecular weight of human insulin is: {:.2f} Da".format(molecularWeightInsulin))

error = (molecularWeightInsulin/molecularWeightInsulinActual - 1) * 100
print("Error percentage : {:.2f}%".format(error))

print()
days = datetime.now() - updated
print("Days since last update: {} days".format(days.days))
#print("Days since last update: {:.0f} days".format(days))
print()