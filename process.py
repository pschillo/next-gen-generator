import numpy as np
import spacy

# specify path to material
path = "materials\chakoteya\StarTrek_NextGen_transcript_complete.txt"

# load material
script = open(path, 'r').read()
