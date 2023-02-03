output = []
#word ending with अनुस्वार   
def anuswar(input_word,n1,suffix):
    r = n1[:-1]
    
    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.2"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Plural"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule - 2.2, Gender - Feminine, Number - Plural")
    
    #return r

#word ending with EEkarant
def EEkarant(input_word,n1,suffix):
    r = n1[:-1]
    if (r[-2]=="ि"):
        r=r[:-2]+"ी"+r[-1]
        #print("Root word / Oblique form: ", r)
    else:
        pass 
        #print("Root word / Oblique form: ", r)
    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.1(b)"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Rule - 2.1(b) , Gender - Feminine, Number - Singular")

def EEkarant2_3(input_word,n1,suffix):
    #print("Root word / Oblique form: ", n1)

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=n1
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.3"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

    #print("Rule - 2.3, Gender - Feminine, Number - Singular")

#word ending with Aekarant
def Aekarant(input_word,n1,suffix):
    r = n1[:-1]
    if (r[-2]=="ि"):
        r=r[:-2]+"ी"+r[-1]
        #print("Root word / Oblique form: ", r)
    else:
        pass
        #print("Root word / Oblique form: ", r)
    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.1(a)"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Rule - 2.1(a) , Gender - Feminine, Number - Singular")

def Aekarant2_4(input_word,n1,suffix):
    r = n1[:-2]
    if len(r)<=2 :
        r = r + "ऊ"
    else:
        r = r + "ू"
    
    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.4"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule - 2.4, Gender - Feminine, Number - Singular")

#word ending with Ookarant
def Ookarant(input_word,n1,suffix):
    if(n1=="बायको"):
        Ookarant2_5(input_word,n1,suffix)
    else:
        #r = n1
        #print("Root word / Oblique form: ", r)
        d ={}
        d[input_word]={}
        d[input_word]["Root_word"]=n1
        d[input_word]["Stem_word"]=n1
        d[input_word]["Rule"]= "1.5"
        d[input_word]["Gender"]= "Masculine"
        d[input_word]["Number"]= "Singular"
        d[input_word]["Suffix"] = suffix
        d[input_word]["Part_of_Speech"] = 'Noun'
        output.append(d)
        return output
        #print("Rule - 1.5, Gender - Masculine, Number- Singular")

#word ending with VAkarant
def VAkarant(input_word,n1,suffix):
    r = n1[:-2]
    if len(r)<=2 :
        r = r + "ऊ"
    else:
        r = r + "ू"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "1.4"
    d[input_word]["Gender"]= "Masculine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule - 1.4, Gender - Masculine, Number - Singular")

def VAkarant2_4(input_word,n1,suffix):
    r = n1[:-3]
    if len(r)<=2 :
        r = r + "ऊ"
    else:
        r = r + "ू"
    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.4"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Plural"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule - 2.4, Gender - Feminine, Number - Plural")

#word ending with YAkarant
def YAkarant(input_word,n1,suffix):
    #exceptions = ['आजोबा', 'दादा', 'काका', 'मामा', 'चहा']
    #for i in exceptions:
    #    if n1==i:
    #        r=n1
    #        break
    

    r = n1[:-3]
    r = r + "ा"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "1.2"
    d[input_word]["Gender"]= "Masculine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule : 1.2 , Gender : Masculine , Number : Singular")

def YAkarant2_3(input_word,n1,suffix):
    r = n1[:-4]
    r = r + "ी"
    
    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.3"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Plural"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule : 2.3 , Gender : Feminine , Number : Plural")

#word ending with AAkarant
def AAkarant(input_word,n1,suffix):
    r = n1[:-1]

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "1.1"
    d[input_word]["Gender"]= "Masculine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
   # print("Root word / Oblique form: ", r)
   # print("Rule : 1.1 , Gender : Masculine , Number : Singular")

def AAkarant2_1a(input_word,n1,suffix):
    r = n1[:-4] +  "ी" + n1[-3:]
    r = r[:-2]
   
    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.1(a)"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Plural"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule : 2.1(a) , Gender : Feminine , Number : Plural")

def AAkarant3_1(input_word,n1,suffix):
    if(n1[1]=="ु"):
        r = n1[0] + "ू" + n1[2:-1]
        r1 = n1[:-1]
    else:
        r = n1[:-1]
        r1 = r

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r, r1
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "3.1"
    d[input_word]["Gender"]= "Neuter"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

    #print("Root word / Oblique form: ", r, ", ",n1[:-1])
    #print("Rule : 3.1 , Gender : Neuter , Number : Singular")

def Aekarant2_2(input_word,n1,suffix):
    r = n1[:-1] + "ा"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.2"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

    #print("Root word / Oblique form: ", r)
    #print("Rule : 2.2 , Gender : Feminine , Number : Singular")

def Ookarant2_5(input_word,n1,suffix):
    #r = n1

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=n1
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.5"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule : 2.5 , Gender : Feminine , Number : Singular")

def VAkarant3_3b(input_word,n1,suffix):
    r = n1[:-2]+ "ू"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "3.3(b)"
    d[input_word]["Gender"]= "Neuter"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

   # print("Root word / Oblique form: ", r)
   # print("Rule : 3.3(b) , Gender : Neuter , Number : Singular")

def YAkarant1_3(input_word,n1,suffix):
    r = n1[:-3]+"ी"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "1.3"
    d[input_word]["Gender"]= "Masculine"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

   # print("Root word / Oblique form: ", r)
   # print("Rule : 1.3 , Gender : Masculine , Number : Singular")

def YAkarant3_2(input_word,n1,suffix):
    r = n1[:-3] + "ी"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "3.2"
    d[input_word]["Gender"]= "Neuter"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

    #print("Root word / Oblique form: ", r)
    #print("Rule : 3.2 , Gender : Neuter , Number : Singular")

def YAkarant3_4(input_word,n1,suffix):
    r = n1[:-3] + "े"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "3.4"
    d[input_word]["Gender"]= "Neuter"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

    #print("Root word / Oblique form: ", r)
    #print("Rule : 3.4 , Gender : Neuter , Number : Singular")

def EEkarant2_1b(input_word,n1,suffix):
    r = n1[:-2]
    
    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.1(b)"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Plural"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output
    #print("Root word / Oblique form: ", r)
    #print("Rule : 2.1(b) , Gender : Feminine , Number : Plural")

def OOkarant2_5(input_word,n1,suffix):
    r = n1[:-2] + "ो"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "2.5"
    d[input_word]["Gender"]= "Feminine"
    d[input_word]["Number"]= "Plural"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

    #print("Root word / Oblique form: ", r)
    #print("Rule : 2.5 , Gender : Feminine , Number : Plural")

def AAkarant3_3a(input_word,n1,suffix):
    r = n1[:-1] + "ू"

    d ={}
    d[input_word]={}
    d[input_word]["Root_word"]=r
    d[input_word]["Stem_word"]=n1
    d[input_word]["Rule"]= "3.3(a)"
    d[input_word]["Gender"]= "Neuter"
    d[input_word]["Number"]= "Singular"
    d[input_word]["Suffix"] = suffix
    d[input_word]["Part_of_Speech"] = 'Noun'
    output.append(d)
    return output

   # print("Root word / Oblique form: ", r)
   # print("Rule : 3.3(a) , Gender : Neuter , Number : Singular")
