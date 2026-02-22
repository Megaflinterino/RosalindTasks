from Bio import Entrez
Entrez.email = "steven.p.rudolf@gmail.com"

geneName = "Enterobacter"
pubDateStart = "2006/03/10"
pubDateEnd = "2012/12/12"
searchTerm = f'({geneName}[Organism]) AND("{pubDateStart}"[Publication Date]: "{pubDateEnd}"[Publication Date])'


Entrez.email = "steven.p.rudolf@gmail.com"
handle = Entrez.esearch(db="nucleotide", term=searchTerm)
record = Entrez.read(handle)
print(record["Count"])