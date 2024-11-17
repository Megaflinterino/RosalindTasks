

original_dna = "insert here DNA snippet"[::-1]

translation_table = str.maketrans('ATCG', 'TAGC')
     
complementary_dna = original_dna.translate(translation_table)

print(complementary_dna)