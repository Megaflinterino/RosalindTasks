from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
#   print(seq_record.id)s
#    print(repr(seq_record.seq))
#    print(seq_record.seq)
#    print(len(seq_record))

max_gc_content = 0.0

#calculates the gc_content of a sequence and if it is bigger then at beginning 0.0 and later the following biggest max_gc_content it gets stored in that variable
for seq_record in SeqIO.parse("/home/steven/Bioinformatik/RosalindTasks/computingGCcontent.fasta", "fasta"):
    #Multiplication with 100 because the output number would be0,...
    gc_content = gc_fraction(seq_record) * 100
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_id = seq_record.id


print(f"{max_gc_id}\n{max_gc_content:.6f}")
