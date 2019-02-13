import spacy


nlp = spacy.load('pt')


ref_arquivo = open("av.txt","r")



text = ref_arquivo.read()
            
        
#nlp = spacy.load('pt')
nlp = spacy.load('pt_core_news_sm')
doc = nlp(text)
#doc = nlp(sentences[0])
#print(doc.text)
#for token in doc:
    #print(token.text, token.pos_, token.dep_)
     #print(token.text)
     #print(doc.ents)
    
##[(entity, entity.label_) for entity in doc.ents]

ENTIDADES = []
for person in doc.ents:
    ENTIDADES.append(person)
print(PESSOAS)
[(i, i.label_) for i in doc.ents]    
