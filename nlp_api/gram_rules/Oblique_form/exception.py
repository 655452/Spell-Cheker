from dataset import *

#Find exception from the list
def isException(input_word, stem_word, suffix):
    output=[]
    flag = False
    for i in Exceptions:
        if(stem_word==i or input_word ==i):
            flag = True
            pos = Exceptions.index(i)
            
            if(0<=pos<=4):
                d ={}
                d[input_word]={}
                d[input_word]["Root_word"]=i
                d[input_word]["Stem_word"]=stem_word
                d[input_word]["Rule"]= "1.2"
                d[input_word]["Gender"]= "Masculine"
                d[input_word]["Number"]= "Singular"
                d[input_word]["Suffix"] = suffix
                d[input_word]["Part_of_Speech"] = 'Noun'
                output.append(d)
                #return (output,True)
                break

            elif(5<=pos<=10):
                d ={}
                d[input_word]={}
                d[input_word]["Root_word"]=i
                d[input_word]["Stem_word"]=stem_word
                d[input_word]["Rule"]= "1.3"
                d[input_word]["Gender"]= "Masculine"
                d[input_word]["Number"]= "Singular"
                d[input_word]["Suffix"] = suffix
                d[input_word]["Part_of_Speech"] = 'Noun'
                output.append(d)
                #return (output, True)
                break
            
            elif(11<=pos<=18):
                d ={}
                d[input_word]={}
                d[input_word]["Root_word"]=i
                d[input_word]["Stem_word"]=stem_word
                d[input_word]["Rule"]= "1.4"
                d[input_word]["Gender"]= "Masculine"
                d[input_word]["Number"]= "Singular"
                d[input_word]["Suffix"] = suffix
                d[input_word]["Part_of_Speech"] = 'Noun'
                output.append(d)
                    #return (output, True)
                    #print("Exception - Rule 1.4")
                break

            elif(19 <= pos <= 21):
                d ={}
                d[input_word]={}
                d[input_word]["Root_word"]=i
                d[input_word]["Stem_word"]=stem_word
                d[input_word]["Rule"]= "2.3"
                d[input_word]["Gender"]= "Feminine"
                d[input_word]["Number"]= "Singular"
                d[input_word]["Suffix"] = suffix
                d[input_word]["Part_of_Speech"] = 'Noun'
                output.append(d)
                    #return (output, True)
                break

            elif(22<=pos<=24):
                d ={}
                d[input_word]={}
                d[input_word]["Root_word"]=i
                d[input_word]["Stem_word"]=stem_word
                d[input_word]["Rule"]= "2.4"
                d[input_word]["Gender"]= "Masculine"
                d[input_word]["Number"]= "Singular"
                d[input_word]["Suffix"] = suffix
                d[input_word]["Part_of_Speech"] = 'Noun'
                output.append(d)
                    #return (output, True)
                break
            else:
                d ={}
                d[input_word]={}
                d[input_word]["Root_word"]=i
                d[input_word]["Stem_word"]=stem_word
                d[input_word]["Rule"]= "n/a"
                d[input_word]["Gender"]= "n/a"
                d[input_word]["Number"]= "n/a"
                d[input_word]["Suffix"] = suffix
                d[input_word]["Part_of_Speech"] = 'n/a'
                output.append(d)
                #output = []
                #flag = False
            break

        else:
            output =[]
            flag = False

    return(output, flag)
