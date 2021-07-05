import numpy as np
import pandas as pd
import csv
#import spacy

# specify path to material
path = "materials\chakoteya\StarTrek_NextGen_transcript_complete.txt"

# specify list of characters
list = ["PICARD", "DATA", "Q", "RIKER", "TROI"]

# process raw text for each character
for name in list:

    # create file name
    title = "quotes_%s.csv" % name
    #print(title)

    # read lines from script into csv
    with open(path) as script:
        with open(title, "w") as file:
            for line in script:
                if line.startswith(name):
                    #print(line)
                    file.write(line)
                    file.write("\n")
