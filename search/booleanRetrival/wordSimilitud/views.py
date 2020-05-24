from django.shortcuts import render
from .forms import WordForm
from django.conf import settings
import time
import gc

nlp = settings.NLP
index = settings.INDEX


#calculates and returns jaccard index
def jaccard(set1, set2):
    len_intersection = len(set1.intersection(set2))
    return len_intersection/(len(set1) + len(set2) - len_intersection)


def calulateSimilarity(request):

    form = WordForm()
    
    if request.method == "POST":
    
        
        form = WordForm(request.POST)
        if form.is_valid():
            # get the word and lowercase it
            _word = form.cleaned_data['word'].lower()


            # lemmatize the word
            doc = nlp(_word)
            lemma_word = " ".join([token.lemma_ for token in doc])

            # check if the word's lemma is indexed
            if lemma_word in index:
                set_word = set(index[lemma_word]) #get the list of the lemmas and cast it to a set, set1
                q = [] 
                start_time = time.time()
                for word in index: # for every item on the index, compare it to the set obtained using the jaccard index
                    set_word_temp = set(index[word]) # cast the list of the word to a set, set2
                    similarity = jaccard(set_word,set_word_temp) # calculate the index jaccar between set1 and set2
                    q.append((similarity, word)) # append the jaccard index and the word to the resulting list

                execution_time = time.time() - start_time

                q.sort(reverse=True) # sort the resulting list by the similarity

                q = q[:100] # get the first 100 results

                return render(request, 'ranking.html', {'form':form,'word':lemma_word,'time': execution_time,'words':q})

            else:

                return render(request, 'ranking.html', {'form':form,'found':'word not indexed'})

        
    return render(request, 'ranking.html', {'form': form})



gc.collect()