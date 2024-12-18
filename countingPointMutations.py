from Bio import Align

s ="CGGCTTCAATCGTTGTGATCGTACATCCCTCCAAACAAATCAGGCGCAGTAGATACGTCTTATAGGGAATCGTCCGAGCGCTCAGCTTCTCCTTTCCCGCCCGGATAGAGGAATTAGTTTCGGCCTGCTTCGCGGGAATTATCTGTGATTACTTTGTCCATGATCCGCGAAGTATACGACCAATCCGTGTCCCATACGCGAGCCTAACGGAACCAACGCGGGGCAACGAAAGCCGGGCGGGGCCGATATGGCGCCGGAATATGAGTGCGCAGCTCCTACTAACCCCGCTAACGATCAAAGAAGCGTCGTAGTATTCGTTAGAGACAGTGAGTGACTCTAAACGGAGCCGGCCCCCTCTTGTCGATCCTTCGAGACCTATTGAAGGGACCTAATCTCAGGTGGTATCGACGAGGCACCAACGCCGCACCATTCTACCAAACCAGGACCTCCTAACTGATTTGCCCCGGCACGTTTCTCTTATCACACCATCCGCATCAATGATCCCTCTTGCACAATGGAAGCCTCCAGCCAGATCATGGTAGATCGGAGCAGGTGAGTATCAAATATTCCTAACCAGGAATCCGGTTTAACCATGCCATAATACCACCTTCTACCACGGGGTACGAGGAATGGCTAACGCTCATCAACGGTTCTCTTCCGCACCAACGACAGAGATCCCCTTCAGAATCGAAGCTCTTGCGTATGAACTTGTATTATCCGGCAGGTTCTTTAACGCTCTGTACAAATCCCCCTAGCGGGCGCTCGTATCACTTACATGATTCTTCCGCACCATTTACTCGGGAAGATAGCAGCCAACAAGAATCACACAGTTCCTGGAGGTTCTTAGTTATGTTGCATCCCAAATGGCGAGCTGGTACATAAACTCTATCGCTCGTGAGGGTGAAACTGATGCTGTCACTGCGTAGAGAGCATATACGTAATAGAGTC"
t= "CCGCTACGCTTTTCCTGATCTTTGCGTCCTTAAAAAAACTGACTGGTAGTAGAAAGATAAGAGAGGCCTTAGTGCATGTACTCTATTTATACGTTGCAGCCGCAATGAATTAATAACTGTACGCCAGCTTCTCTGTATTTATGTCTGAAGCCTACCTGGTCCATGCCTTGTGAACAAGCAAAATCAGCTCCGGAAATGGATTCTTTGCTGACTAAATAACGGGGCGGGTAACCGGGGCGAGGCCGACAGGTGGACGGACCATTACTGAGCACTTACTATCGTACCCCCTTACGCGGCCAGTAGAGCCGATGTTTTATTTCCCCAGGATAATGGAGTCAAACGCGATCAGGCCCGTCATACATGATTGCCGATGTCCAATGGAAAGCAGTTTTAACCGACAGATAGCCATGAGCAACTAACGCGGACTCATTATACTATCTCAATACTGGCCTAGTCATGGGTGTCTCTACGTGATTCTCGGCAGGCTATGTTACACTATAATCGGTTGAGTAAAAACATGGCCTCGACACTAAGTGTAGTAGAACCGGCAGGCAGTACGTCAATGTTTGACATTCGGTGGACGGGTTTTATAGTCCGATCGTGTTACCTTTTACCTAGGAGGACATAGTATTCCTAAAGTTTCTCTTAAGTCGAACAGCCTAACAACGACAGCGATCTCCAAAAGGATTTAAGGATTGGGGTACGTGAGGGCATACTGCCCCATGGCTTATGCAACTCCGTACGTTGGTCAATCGGGGTATATCGTTACTCCTAAAAGAACCGCTATAACCACAGACCGGGACTGCCACTAGGGAAAAAGTTGCAAACATACCCCACTCTTTCCACCATTGGTTCCATCCCAACTGAAAAGGTGTCGTTATACTTAAGTCGATTGAGATCGGGGGTGGACTAACGAAAGTCCAGCGGTTCGAAAGACTGCGGAGAGTT"

distance = 0
L = len(s)
for i in range(L):
    if s[i] != t[i]:
        distance += 1

print(distance)

