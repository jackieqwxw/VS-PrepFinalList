## Headers
####################################################################
#  Prepare the final hit list from SD files for virtual screening  #
#  Computational Biophysics & Drug Design (Kireev lab)             #
#  Developed by Xiaowen Wang                                       #
####################################################################

import sys
import csv

inputfile1 = sys.argv[1]
inputfile2 = sys.argv[2]
outputfile = sys.argv[3]

# Read data from inputfile.csv and store it in a dictionary
cluster_rep_350 = {}
with open(inputfile1, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row if present
    for row in csvreader:
        cluster_id, smiles, name, gscore, adscore, cluster_size, remove = row 
        cluster_rep_350[name] = {'cluster_ID': cluster_id, 'cluster_size': cluster_size}
        
with open(inputfile2, 'r') as f:
    sd_data = f.read().split("$$$$\n")  # Split SD file into individual compounds

updated_compounds = []
# Iterate over names from CSV and select compounds from SDF file
for name, info in cluster_rep_350.items():
    cluster_size = info['cluster_size']
    cluster_id = info['cluster_ID']

    for compound in sd_data:
        lines = compound.strip().split('\n')
        name_line = lines[0].strip()  # name is the first line in SD file
        if name_line == name:
            # Add cluster size and ID information to the compound
            lines.append('\n> <Cluster_ID>\n' + cluster_id + '\n')
            lines.append('> <Cluster_Size>\n' + cluster_size + '\n\n')
            # Join the lines back into a compound and add to updated_compounds list
            updated_compound = '\n'.join(lines)
            updated_compounds.append(updated_compound)
            break

# Write the selected compounds to updated_compounds.sdf
with open(outputfile, 'w') as f:
    f.write('$$$$\n'.join(updated_compounds) + '$$$$\n')
