import numpy as np
import pandas as pd
import csv
#import spacy

# specify path to material
path = "materials\chakoteya\StarTrek_NextGen_transcript_complete.txt"

## read Picard's lines from script into csv
with open(path) as script:
    for line in script:
        if line[0] == "PICARD":
            writer = csv.writer("quotes_PICARD.csv")
            writer.writerow(line)
