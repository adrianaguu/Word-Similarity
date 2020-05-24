#lematize the words on google corpus file using spacy

from nltk.corpus import wordnet
import spacy
import io

nlp = spacy.load('en', disable=['parser', 'ner'])

for i in range (0,32):
    file_name = "2gm-00" + str(i)
    file = io.open(file_name,'r', encoding="utf-8")                         
    lines = file.readlines()


    file_lemas = open("lemas/"+file_name+"-lemas",'w', encoding="utf-8") 

    for line in lines:
        line.strip('\n')
        line = line.split(' ')
        # get the words 
        first_word = line[0].lower()
        second_word = line[1].split('\t')[0].lower()
        doc = nlp(first_word + ' ' + second_word)
        ocurrecies = line[1].split('\t')[1]
        
        #if both words are in english, lemmatize them and save them in the new file
        if wordnet.synsets(first_word) and wordnet.synsets(second_word):
            lemmas = " ".join([token.lemma_ for token in doc])
            file_lemas.write(lemmas + ' '+ ocurrecies)
