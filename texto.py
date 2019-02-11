#------------------------------------------------------------------------------
# Author:      wfpne
#
# Created:     31/01/2019
# Copyright:   (c) wfpne 2019
# Licence:     <your licence>
#------------------------------------------------------------------------------


import spacy
from os import path

nlp = spacy.load('pt')

TextFile = path.join(path.dirname(path.realpath(__file__)), "mnrlc.txt")
# Process whole documents
#text = (".")
texto = open(TextFile, 'r')
text = texto.read()
doc = nlp(text)
        
PESSOAS = []
for person in doc.ents:
    PESSOAS.append(person)
print(PESSOAS)
#for token in doc:
#    print(token.text, token.pos_, token.dep_)
    
# Determine semantic similarities
#doc1 = nlp(u"my fries were super gross")
#doc2 = nlp(u"such disgusting fries")
#similarity = doc1.similarity(doc2)
#print(doc1.text, doc2.text, similarity)