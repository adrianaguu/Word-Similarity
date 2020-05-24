# Generates the dictionary that stores the words their respective lists 
# the dictionaty is saved using the pickle library

import pickle


# gets the first word of a line in the file
def getfirstWord(line):
    line = line.split(' ')
    first_word = line[0]
    return first_word


# gets the second word of a line in the file
def getsecondWord(line):
    line = line.split(' ')
    second_word = line[1]
    for i in range (2,len(line)-1):
        second_word += " " + line[i]
    return second_word


#create the empty dictionary
index = {}

#iterate through the google corpus lematized factorized files
for k in range (1,32):
    filefact = open("../factorized/2gm-00"+str(k)+"-lemas-facto")
    lines = filefact.readlines()
    i = 0
    #iterate though the file's lines
    while i<len(lines):
        line = lines[i]
        first_word = getfirstWord(line)
        second_word = getsecondWord(line)

        context = [second_word] #the list containing the matched words with the line's first word

        # the lines are sorted, so we iterate asking if the next line's first word is equal to the
        # current line's first word, is so, we add the next line's second word to the list
        while(i+1<len(lines) and first_word == getfirstWord(lines[i+1])):
            context.append(getsecondWord(lines[i+1]))
            i+=1
        # update de dictionary adding the word as the key, and it's respective list as the value
        index.update({first_word:context})
        i+=1


# save the generated dictionary in a file named 'index' unsing pickle
filename = 'index'
outfile = open(filename,'wb')
pickle.dump(index,outfile)
outfile.close()