from dataset import *

#Find Gramnaam from dictionary
def isGramnam(input_word, stem_word, suffix):
    output = []
    flag =False
    if input_word in Gramnam:
        
        if(Gramnam[input_word]== "कोलकाता" or Gramnam[input_word]=="बडोदा"):
            flag = True 
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Gramnam[input_word]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "5.1"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)
            #return (output, flag)
        
        elif(Gramnam[input_word] == "दिल्ली" or Gramnam[input_word] == "मुंबई"):
            flag = True 
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Gramnam[input_word]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "5.2"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)
            #return (output, flag)

        elif(Gramnam[input_word] == "पुणे" or Gramnam[input_word] == "पेडणे"):
            flag = True
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Gramnam[input_word]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "5.3"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)
            #return (output, flag)

        elif(Gramnam[input_word] == "नागपूर" or Gramnam[input_word] =="सोलापूर"):
            flag = True
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Gramnam[input_word]
            d[input_word]["Stem_word"]= stem_word
            d[input_word]["Rule"]= "5.4"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)
            #return (output, flag)
        else:
            output = []
            flag = False
    else:
        output = []
        flag = False
    return (output, flag)
         
        
        
