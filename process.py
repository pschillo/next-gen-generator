import numpy as np
import pandas as pd
import csv
#import spacy

# specify path to material
path = "materials\chakoteya\StarTrek_NextGen_transcript_complete.txt"

## read Picard's lines from script into csv
with open(path) as script:
    with open("quotes_PICARD.csv", "w") as file:
        for line in script:
            if line.startswith("PICARD"):
                print(line)
            #with open("quotes_PICARD.csv", "wb") as file:
                file.write(line)
                file.write("\n")
                #writer = csv.writer(file)
                #writer.writerow(line)
