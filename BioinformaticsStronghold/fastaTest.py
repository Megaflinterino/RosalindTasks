from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

for seq_record in SeqIO.parse("/home/steven/Bioinformatik/RosalindTasks/computingGCcontent.fasta", "fasta"):
     def GC(sequence):
        return 100 * gc_fraction(sequence, ambiguous="ignore")
     print(GC(seq_record))