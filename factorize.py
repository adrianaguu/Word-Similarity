#factorize the ocurrencies

import io

def getfirstWord(line):
    line = line.split(' ')
    first_word = line[0]
    return first_word


def getsecondWord(line):
    line = line.split(' ')
    second_word = line[1]
    for i in range (2,len(line)-1):
        second_word += " " + line[i]
    return second_word

def getOcurrencies(line):
    line = line.split(' ')
    ocurrecies = line[len(line)-1]
    return int(ocurrecies)


for i in range (0,32):
    file_name = "2gm-00" + str(i) + "-lemas"
    file = io.open("lemas/"+file_name,'r', encoding="utf-8")
    #read the lines and sort them
    lines = file.readlines()
    lines.sort()


    file_factorized = io.open("factorized/"+file_name + "-facto",'w',encoding="utf-8")

    #iterate through the lines
    i = 0
    while i<len(lines):
        line = lines[i]
        first_word = getfirstWord(line)
        second_word = getsecondWord(line)
        ocurrecies = getOcurrencies(line)
        # while the first word and second word of two conseutive lines, are the same, add their ocurrencies
        while(i+1<len(lines) and first_word ==  getfirstWord(lines[i+1]) and second_word == getsecondWord(lines[i+1])):
            ocurrecies += getOcurrencies(lines[i+1])
            i+=1

        # write the new line with the ocurrencies calculated
        file_factorized.write(first_word+' '+second_word+' '+str(ocurrecies)+'\n')
        i+=1

    
         




