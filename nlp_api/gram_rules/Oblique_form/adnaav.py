from dataset import *

#Find Adnaav from dictionary
def isAdnav(input_word, stem_word, suffix):
    output = []
    flag = False
    if input_word in Surname:
        
        if(Surname[input_word] =="देशपांडे" or Surname[input_word] =="कोल्हे" or Surname[input_word] =="आठवले"  or Surname[input_word] =="पालवे"):
            flag = True
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Surname[input_word]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "4.1"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)
            
        elif(Surname[input_word]=="खेर" or Surname[input_word]=="केळकर" or Surname[input_word]=="गायकवाड" or Surname[input_word]=="भट"):
            flag = True
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Surname[input_word]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "4.2"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)
            
        elif(Surname[input_word]=="साधू" or Surname[input_word]=="कडू"):
            flag = True
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Surname[input_word]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "4.3"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)

        elif(Surname[input_word]=="बोरा" or Surname[input_word]=="कटारिया"):
            flag = True
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Surname[input_word]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "4.4"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)

        elif(Surname[input_word]=="घवी" or Surname[input_word]=="वाणी"):
            flag = True
            d ={}
            d[input_word]={}
            d[input_word]["Root_word"]=Surname[input_word]
            d[input_word]["Stem_word"]=stem_word
            d[input_word]["Rule"]= "4.5"
            d[input_word]["Gender"]= "n/a"
            d[input_word]["Number"]= "n/a"
            d[input_word]["Suffix"] = suffix
            d[input_word]["Part_of_Speech"] = 'Noun'
            output.append(d)
        
        else:
            output = []
            flag = False                   
    else:
        output = []
        flag = False
    return (output, flag)
        

            