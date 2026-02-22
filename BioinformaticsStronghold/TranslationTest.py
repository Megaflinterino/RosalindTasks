inputDNA = "Hello World"

translationTable = str.maketrans('Hel', 'Ga1')
     
complementaryDNA = inputDNA.translate(translationTable)

print(complementaryDNA)