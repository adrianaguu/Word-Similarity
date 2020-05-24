from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer 
import io
import nltk

def get_wordnet_pos(treebank_tag):

	if treebank_tag.startswith('J'):
		return wordnet.ADJ
	elif treebank_tag.startswith('V'):
		return wordnet.VERB
	elif treebank_tag.startswith('N'):
		return wordnet.NOUN
	elif treebank_tag.startswith('R'):
		return wordnet.ADV
	else:
		return None


lemmatizer = WordNetLemmatizer() 

file_name = "2gm-0000"
file = io.open(file_name,'r', encoding="utf-8")
lines = file.readlines()


file_lemas = open("finale/"+file_name+"-lemas",'w', encoding="utf-8") 

for line in lines:

	line = line.split('\t')
	bigram = line[0].lower()
	ocurrecies = line[1]
	nltk_tagged = nltk.pos_tag(nltk.word_tokenize(bigram))
	wn_tagged = list(map(lambda x: (x[0], get_wordnet_pos(x[1])), nltk_tagged))
	first_word_prop = wn_tagged[0]
	second_word_prop = wn_tagged[1]

	first_word = first_word_prop[0]
	second_word = second_word_prop[0]

	if wordnet.synsets(first_word) or wordnet.synsets(second_word):
		first_lemma = first_word
		second_lemma = second_word
		if (first_word_prop[1]):
			first_lemma = lemmatizer.lemmatize(first_lemma,first_word_prop[1])
		if (second_word_prop[1]):
			second_lemma = lemmatizer.lemmatize(second_lemma, second_word_prop[1])
		file_lemas.write(first_lemma + ' ' + second_lemma + ' '+ ocurrecies)

	