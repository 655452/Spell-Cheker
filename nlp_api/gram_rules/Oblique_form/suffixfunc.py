from dataset import *

#Find suffix and remove it
def issuffix(input_word):
    for i in suffixtuple:
        if (input_word.endswith(i)==True) :
            stem_word= input_word[:-len(i)]
            suffix = i
            #print(stem_word)
            break
            
        else:
            stem_word = input_word
            suffix = "n/a"  #if suffix is not present

    return(stem_word,suffix)


            
            





