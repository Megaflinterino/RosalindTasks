def CopyEvenLines(input, output):

#Opens both files simultaniously
    with open(input, 'r') as infile, \
            open(output, 'w') as outfile:

            #Every line gets enumareted and if the linenumber is even it gets copied to output
            for zeilennummer, zeile in enumerate(infile, start=1):
                if zeilennummer % 2 == 0:
                    outfile.write(zeile)

#calls the function
CopyEvenLines('rosalind_ini5.txt', 'output.txt')