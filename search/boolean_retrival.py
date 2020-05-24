import pickle
import heapq
import time
import spacy



def jaccard(set1, set2):
    len_intersection = len(set1.intersection(set2))
    return len_intersection/(len(set1) + len(set2) - len_intersection)



filename = 'index'
infile = open(filename,'rb')
index = pickle.load(infile)
infile.close()

dog = set(index["dog"])

q = []
start_time = time.time()
for word in index:
    set_word = set(index[word])
    simility = jaccard(dog,set_word)
    heapq.heappush(q,(-simility, word))

print("--- %s seconds ---" % (time.time() - start_time))


num_lemas = len(index)
#for i in range(1,100):
#    print(q[i])

print(num_lemas)


