
##DNA = "GATATATGCATATACTT"
##motif = "ATAT"

import re
#motif = "ATAT"
dna = "GATATATGCATATACTT"

#for i in re.finditer(motif,dna):
#    print(i.start()+1)

for i in range(len(dna)):
    if  dna[i:] .startswith("ATAT"):
        print(i+1)