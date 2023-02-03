from verb_dataset import *

def isVerb(input_word, stem_word, suffix):
    output=[]
    flag = False
    for vb in verb:
        if stem_word==vb:
            #print(vb, verb[vb])
            flag = True
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=verb[vb]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "n/a"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Verb'
            output.append(d)
            #print(output)
            #return (output,True)
            break
        else:
            output = []
            flag = False
    return(output, flag)
        
