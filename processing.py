#import numpy as np
#import pandas as pd
import csv
import spacy

# specify path to material
path = "materials\chakoteya\StarTrek_NextGen_transcript_complete.txt"

# specify list of characters
list = ["PICARD", "DATA", "Q", "RIKER", "TROI"]

def process(list,path):
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

# paths to newly created .csv's (same order as characters in 'list'!)
filepaths = ["quotes_PICARD.csv", "quotes_DATA.csv", "quotes_Q.csv", "quotes_RIKER.csv", "quotes_TROI.csv"]
testlist = ["quotes_PICARD.csv"]

def keywords(list):

    # process each of the files from the list
    for path in list:

        # read file
        with open(path) as file:
            filereader = csv.reader(file)
            #print("file was read")

            # per row
            for row in filereader:

                # concatenate row to string
                string = "".join(str(x) for x in row)
                #print(string)

                # load spacy
                nlp = spacy.load("en_core_web_sm")
                doc = nlp(string)

                # collect lemmas
                lemmas = [word.lemma_ for word in doc]
                #for word in doc:
                #lemmas.append(row.lemma_)
                print(lemmas)

                # add lemmas as new column
                ##row.append(lemmas)

            print("this is where the keyword function goes")

def main():

    # process raw data
    #process(list,path)
    print("raw data has been processed")

    # test keyword function
    keywords(testlist)
    print("keyword function has been tested")

if __name__ == "__main__":
    main()
