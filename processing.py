#import numpy as np
import pandas as pd
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
testlist = ["testfile.csv"]

def keywords(list):

    # process each of the files from the list
    for path in list:

        # convert to dataframe
        dataframe = pd.read_csv(path, names=["line"])
        dataframe = dataframe.dropna()
        print(dataframe)

        all_lemmas = []

        # read file
        with open(path) as file:
            filereader = csv.reader(file)

            # per row
            for row in filereader:

                # concatenate row to string
                string = "".join(str(x) for x in row)

                # load spacy
                nlp = spacy.load("en_core_web_sm")
                doc = nlp(string)

                # collect lemmas
                lemmas = [word.lemma_ for word in doc]

                # add lemmas as new column
                all_lemmas.append(lemmas)
                print("done")

        # clean list of all lemmas
        all = [list for list in all_lemmas if list != []]
        print(all)

        # add as second column
        dataframe.insert(1, "lemmas", all)
        print(dataframe)

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
