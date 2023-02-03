from .variables import *
# from .Oblique_form import main
#################################################################################
# print("-----------------RULES---------------------")


def print_rule(word, rule):
    return [word, rule]


######################################################################################
# RULE 1 CORECT WORD FORMER:


# def correct_word(word, resp):
#     try:
#         if word[1] == 'ू' or word[1] == 'ु' or word[1] == 'ी' or word[0] == 'ि':
#             if resp:
#                 word1 = word[0:2] + 'ं' + word[2:]
#                 return word1

#             else:
#                 word1 = word[0:-1] + 'ं' + word[-1]
#                 return word1
#         else:
#             if resp:
#                 word1 = word[0]+'ं'+word[1:]
#                 return word1
#             else:
#                 word1 = word[0:-1]+'ं'+word[-1]
#                 return word1
#     except:
#         pass
######################################################################################

def r1a(word, rule):
    word = word.strip()
    # cnt += 1
    # print(f'Fn call {cnt}')
    if(any(x in word for x in 'ं')):
        try:
            if(word[1] == 'ं'):
                return True
            if(word[-2] in CONSONANTS):
                ind = word.index(word[-2])
                # print(ind)
                if(word[ind-1] == 'ं'):
                    return True
            elif(word[-1] in CONSONANTS):
                ind = word.index(word[-1])
                if(word[ind-1] == 'ं'):
                    return True

            return False
        except:
            return False

    try:
        if(word[-2] in CONSONANTS):
            return False
    except:
        pass
    else:
        return None
##########################################################################
# RULE 1:b


def r1b(word, rule):
    word = word.strip()
    if(any(x in word for x in 'ं')):
        for x in word:
            try:
                if x == 'ं' or x == '्':
                    index = word.index(x)
                    if word[index+1] in VELAR_CONSONANTS:
                        return [True, index+1]
                    elif word[index+1] in PALATAL_CONSONANTS:
                        return [True, index+1]
                    elif word[index + 1] in RETROFLEX_CONSONANTS:
                        return [True, index+1]
                    elif word[index+1] in DENTAL_CONSONANTS:
                        return [True, index+1]
                    elif word[index+1] in LABIAL_CONSONANTS:
                        return [True, index+1]
            except:
                pass
        else:
            return [False, None]
    else:
        return [None, None]
##########################################################################
# RULE 1 : c


def r1c(word, rule):
    word = word.strip()
    if(any(x in word for x in 'ं')):
        try:
            for x in word:
                if x in SHUDH_CONSONANTS:
                    if x == word[0]:
                        pass
                    else:
                        index = word.index(x)
                        if word[1] == "ं":
                            return [True, None]
                        elif word[index-1] == "ं":
                            return [True, None]
                        else:
                            if (any(item in word for item in "ं")):
                                return [True, None]
                            else:
                                return [False, index]
            else:
                return None
        except:
            return None
    else:
        return None
##########################################################################
# Rule 1 : d

# use of stemmer comes in play


# def r1d(word, rule):
#    word = word.strip()
 #   if any(item in IS for item in word[-1]) or if any(item in VP for item in word):

###########################################################################################

######################################################################################
# rule 2a
# exception - ni rasva
def r2a(word, rule):
    word = word.strip()
    try:
        if len(word) == 2:
            if word[-1] == EE_RASVA:
                return False

            elif word[-1] == UU_RASVA:
                return False
            elif word == "णि" or word == "नि":
                return True
            else:
                return True
        else:
            return None
    except:
        pass
######################################################################################
# rule 2b

# "aai word handling -- len(2)"


def r2b(word, rule):
    word = word.strip()
    try:
        if word[-1] == E_RASVA:
            return False
        elif word[-1] == EE_RASVA:
            return False
        elif word[-1] == U_RASVA:
            return False

        elif word[-1] == UU_RASVA:
            return False
        else:
            return True
    except:
        pass
###############################################################

# RULE 2 : C
# The equivalent and ‘imported as they are’ words ending with long
# vowel इ and vowel उ like कपव, रर,गर,वाय
# ,प्रीतत are pronounced with long
# ending vowel, compatible with the nature of Marathi language
# e.g. as in गडकरी ेकवी ोते, री व मध
# ूघरी गेले, ग्रंथ ेच खरेग
# र ोत.
########################################################


def r2c(word, rule):

    word = word.strip()
    try:
        if word[-1] in ALL_RD or word[1] in ALL_RD:
            if word[-1] in EE_RASVA or word[-1] in UU_RASVA or word[1] in EE_RASVA or word[1] in UU_RASVA:
                return False

            elif word[-1] in UU_DIRGHA or word[-1] in EE_DIRGHA or word[1] in UU_DIRGHA or word[1] in EE_DIRGHA or word[-1] == "ई":
                return True
            else:
                return False
    except:
        return None
############################################################

# r2c(word="कवीराज")

###########################################################
# words example = ['गुरु','कवि','हरि','वायु','प्रिती']
###########################################################

# RULE 2 : d
# Though names of person, book names, titles, free words (‘imported as
# they are’ from Sanskrit to Marathi) are basically ‘ending with short
# vowel’, They should be written ‘ending with long vowel’

###########################################################

# RULE 2 : e


def r2e(word, rule):
    word = word.strip()
    Flag = False
    index = 0
    for x in word:
        try:
            if x == EE_RASVA or x == UU_RASVA:
                print_rule(word, rule)
                Flag = True
                break
            elif x == EE_DIRGHA or x == UU_DIRGHA:
                print_rule(word, rule)
                index = word.index(x)
                Flag = False
                break
            else:
                Flag = None
        except:
            pass

    if Flag != None:
        if Flag:
            return [True, None]
        else:
            if len(word) < 3:
                index = 1
                return [False, index]
            else:
                if index:
                    index = 2
                    return [False, index]

# r2e(word="मृत्यूलेख")
################################################################
# words_example = ['गुरूदक्षिणा','वायुपुत्रा',''मृत्युलेख','भानूविलास','गतिमान','हरिकृपा']
################################################################

# RULE 2 : f
# First Syllable in compound word contain long vowel , then let it long vowel
#######################################################################


def r2f(word, rule):
    word = word.strip()
    Flag = False
    index = 0
    for x in word:

        if x in ["ू", "ी"]:
            # print_rule(word, rule)
            # print("Valid Syntax")
            # break
            index = 1
            Flag = True
            break
            # return [True, index]
        elif x in ["ु", "ि"]:
            # print_rule(word, rule)
            index = word.index(x)
            # print("Invalid Syntax :: [ ", word[index],
            #       " ] Make it EE_DIRGHA [ ", EE_DIRGHA, " ]")
            # break
            Flag = False
            break
            # return [False, index]

        else:
            Flag = None
    # print(Flag)

    if Flag != None:
        if Flag:
            return [True, 1]
        else:
            return [False, index]

# r2f(word="पृथ्वीतल")
# #original word 'पृथ्वीतल''पृथ्वितल'
# #############################################################
# word = 'विध्यार्थिन्'
# x = word.strip()
# for x in word:
#     print(x)
############################################################


def r2g(word, rule):
    word = word.strip()
    try:
        if VIRAMA in word[-1] and word[-2] == "न":
            print_rule(word, rule)
            return False
        else:
            return None
    except:
        return None
# r2g  (word='विध्यार्थिन्')

##############################################################
# RULE 2h


def r2h(word, rule):
    word = word.strip()
    print_rule(word, rule)
    try:
        if word in INVARIABLE or word in INDECLINABLE:
            return True
        else:
            return None
    except:
        pass
# r2h (word='परंतू')


######################################################################################
######################################################################################
"""
Rule 3 :
    sub rule 1 ::  follows
    sub rule 2 ::  Sanskrit Exception
    sub rule 3 ::  follows
    sub rule 4 ::  Sanskrit Exception
"""


######################################################################################
# rule 3a
def r3a(word, rule):
    word = word.strip()
    try:
        if word[-1] not in DEV_VOWELS:
            if word[-2] == E_RASVA:
                return False

            elif word[-2] == EE_RASVA:
                return False

            elif word[-2] == U_RASVA:
                return False

            elif word[-2] == UU_RASVA:
                return False

            elif word[-2] in UU_DIRGHA or word[-2] in EE_DIRGHA:
                return True
    except:
        return None
######################################################################################
# rule 3b
# Hardcode


def r3b(word, rule):
    dc = {
        "गुण": "गूण",
        "युग": "यूग",
        "विष": "वीष",
        "प्रिय": "प्रीय",
        "मधुर": "मधूर",
        "बहुत": "बहूत",
        "मंदिर": "मंदीर",
        "अनिल": "अनील",
        "परिचित": "परिचीत",
        "स्थानिक": "स्थानीक",
        "बुध": "बूध",
        "सुख": "सूख",
        "हिम": "हीम",
        "शिव": "शीव",
        "कुसुम": "कूसुम",
        "तरुण": "तरुन",
        "रसिक": "रसीक",
        "चतुर": "चतूर",
        "नागरिक": "नागरीक",
        "सामाजिक": "सामाजीक"
    }
    word = word.strip()
    flag = 0
    for i in dc:
        if word == dc[i]:
            flag = 1
            correct_wrd = i
            return [False, correct_wrd]


######################################################################################
# rule 3c
DIRGH = ['ा', 'ॅ', 'ी', 'ॉ', 'ू', 'ॆ', 'े', 'ै', 'ॊ', 'ो', 'ौ']


def r3c(word, rule):
    word = word.strip()
    try:
        if word[-1] in DIRGHA:
            if len(word) > 2:

                if word[-3] == E_DIRGHA:
                    print_rule(word, rule)
                    return False

                elif word[-3] == EE_DIRGHA:
                    print_rule(word, rule)
                    return False

                elif word[-3] == U_DIRGHA:
                    print_rule(word, rule)
                    return False

                elif word[-3] == UU_DIRGHA:
                    print_rule(word, rule)
                    return False
                else:
                    # print_rule(word, rule)
                    if word[1] in ALL_RASVA or word[3] in ALL_RASVA:
                        return True
        elif word[3] == UU_DIRGHA or word[3] == EE_DIRGHA:
            return False
        else:
            return None
    except:
        pass

###########################################################################################
# rule r3d hardcode


def r3d(word, rule):
    dc = {
        "पूजा": "पुजा",
        "भीती": "भिती",
        "प्रीती": "प्रिती",
        "पूर्व": "पुर्व",
        "दीप": "दिप",
        "पीडा": "पिडा",
        "नवीन": "नविन",
        "संगीत": "संगित",
        "लीला": "लिला",
        "नीती": "निती",
        "कीर्ती": "किर्ती",
        "चूर्ण": "चुर्ण",
        "नीच": "निच",
        "क्रीडा": "क्रिडा",
        "शरीर": "शरिर",
        "परीक्षा": "परिक्षा"
    }
    word = word.strip()
    flag = 0
    for i in dc:
        if word == dc[i]:
            flag = 1
            correct_wrd = i
            return [False, correct_wrd]
    if flag != 1:
        if word[1] in DIRGHA or word[3] in DIRGHA:
            return [True, word]

###########################################################################################


def r4a(word, rule):
    word = word.strip()
    try:
        if len(word) > 2:
            if word[-1] in DIRGH:
                if word[-3] == E_RASVA:
                    return False

                elif word[-3] == EE_RASVA:
                    print_rule(word, rule)
                    return False

                elif word[-3] == U_RASVA:
                    print_rule(word, rule)
                    return False

                elif word[-3] == UU_RASVA:
                    print_rule(word, rule)
                    return False
                else:
                    return None
        else:
            return None
    except:
        pass
##############################################################################


def r4b(word, rule):
    word = word.strip()
    try:
        if word[-1] in DIRGH:
            if len(word) > 2:
                if word[-3] == E_DIRGHA:
                    return False

                elif word[-3] == EE_DIRGHA:
                    return False

                elif word[-3] == U_DIRGHA:
                    return False

                elif word[-3] == UU_DIRGHA:
                    return False
                else:
                    return None
            else:
                return None
    except:
        pass

#########################################################################################
# rule 4c - hardcode


# def r4c(word, rule):
#     word = word.strip()
#     res = main()
#     return res
#########################################################################################
# rule5b - hardcode , aahe- hahe


def r5b(word, rule):
    word = word.strip()
    dc = {
        "नागपूर": "नागपुर",
        "एखादा": "एकादा",
        "कोणता": "कोणचा",
        "हळूहळू": "हळुहळू",
        "तसूतसू": "तसुतसू",
        "मुळूमुळू": "मुळुमुळू"
    }
    for i in dc:
        if word == dc[i]:
            crct = i
            return [False, crct]
        elif word == i:
            return [True, word]

#########################################################################################
# rule5d - hardcode


def r5d(word, rule):
    word = word.strip()
    dc = {
        "अर्थात्": "अर्थात",
        "कचीत्": "कचीत",
        "तस्मात्": "तस्मात",
        "साक्षात्": "साक्षात",
        "विद्वान्": "विद्वान",
        "कदाचित्": "कदाचित",
        "परिषद्": "परिषद",
        "पश्चयात्": "पश्चयात",
        "किंचित्": "किंचित",
        "विद्युत्": "विद्युत",
        "सम्राट्": "सम्राट",
        "श्रीमान्": "श्रीमान",
        "भगवान्": "भगवान",
        "प्रतिष्ठ्": "प्रतिष्ठ",
        "संसद्": "संसद"
    }
    for i in dc:
        if word == dc[i]:
            crct = i
            return [False, crct]
#########################################################################################
# rule 5f- an


def r5f(word, rule):
    word = word.strip()
    if(word == "हि"):
        crct = "ही"
        return [False, crct]
    elif(word == "अन्"):
        crct = "अन"
        return [False, crct]
    elif(word == "ही"):
        return [True, word]
    elif(word == "अन"):
        return [True, word]
    else:
        return [None, None]

#########################################################################################

# RULE 5 : e


def r5e(word, rule):
    word = word.strip()
    try:
        if word in turki_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in english_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in portuges_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in farshi_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in arbi_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in kandi_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in gujarati_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in hindi_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in telugu_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in tamil_word:
            # print_rule(word, rule)
            # print("valid syntax")
            return True
        else:
            return False
    except:
        return None

#########################################################################################


def execute_others(temp, word, correct, incorrect, rule_dict):
    x_list = []

    for x in temp:
        if x in ALL_RD:
            x_list.append(x)

    # ----------------RULE 2-----------------------------
    try:
        if len(temp) < 3 and any(item in x_list for item in DEV_VOWELS):
            rule = "r2a"
            r2arule = r2a(word, rule)
            if r2arule != None:
                # print("###################################")
                if r2arule:
                    rule = "r2a"
                    correct.append(rule)
                else:
                    rule = f"r2a"
                    incorrect.append(rule)
    except:
        pass
    try:
        if word[-1] in ALL_RD and any(item in x_list for item in DEV_VOWELS) or any(item in x_list for item in STD_VOWELS):
            rule = 'r2b'
            if word[0] == 'अ' and word[-1] == "ई":
                rule = 'r2b'
                # rule = 'Category:  End Letters\nr2b: Correct word will be आई'
                incorrect.append(rule)
            else:
                rule = 'r2b'
                r2brule = r2b(word, rule)
            # print("###################################")
                if r2brule:
                    rule = 'r2b'
                    # rule = "Category:  End Letters\nr2b : Valid Syntax contains proper DIRGHAS"
                    correct.append(rule)
                else:
                    rule = 'r2b'
                    # rule = f"Category:  End Letters\nr2b: Invalid Syntax:: {word[-1]} E_RASVA/EE_RASVA/U_RASVA/UU_RASVA change it to E_DIRGHA {E_DIRGHA}/{EE_DIRGHA}/{U_DIRGHA}/{UU_DIRGHA}"
                    incorrect.append(rule)
    except:
        pass
    # ---------------------RULE 3--------------------------
    try:
        if temp[-1] in CONSONANTS:
            rule = 'r3a'
            r3arule = r3a(word, rule)
            if r3arule != None:
                try:
                    if r3arule:
                        rule = 'r3a'
                        # rule = "Category: PenUltimate Letters \nr3a: Valid Syntax contains proper DIRGHAS"
                        correct.append(rule)
                    else:
                        rule = 'r3a'
                        # rule = f"""Category: PenUltimate Letters \nr3a: Invalid Syntax :: {word[-2]} E_RASVA/EE_RASVA/UU_RASVA/U_RASVA change it to E_DIRGHA/EE_DIRGHA/U_DIRGHA/UU_DIRGHA {E_DIRGHA}/{EE_DIRGHA}/{U_RASVA}/{UU_RASVA}.If word is tatsam leave as it is !!"""
                        incorrect.append(rule)
                except:
                    # rule = f"""Category: PenUltimate Letters \nr3a: Invalid Syntax :: E_RASVA/EE_RASVA/UU_RASVA/U_RASVA change it to E_DIRGHA/EE_DIRGHA/U_DIRGHA/UU_DIRGHA {E_DIRGHA}/{EE_DIRGHA}/{U_RASVA}/{UU_RASVA}.If word is tatsam leave as it is !!"""
                    incorrect.append(rule)
    except:
        pass
        # print("###################################")
        rule = 'r3b'
        ret = r3b(word, rule)
        if ret != None:
            r3brule = ret[0]
            crct = ret[1]
            # print("###################################")
            if r3brule != None:
                if r3brule:
                    rule = 'r3b'
                    correct.append(rule)
                else:
                    rule = 'r3b'
                    incorrect.append(rule)
    try:
        # print(temp[-2])
        if temp[-2] in CONSONANTS or temp[-3] in CONSONANTS and any(item in x_list for item in DIRGHA):
            rule = 'r3c'
            # print(rule)
            r3crule = r3c(word, rule)
            # r3d(word)
            if r3crule != None:
                if r3crule:
                    rule = 'r3c'
                    correct.append(rule)
                else:
                    rule = 'r3c'

                    incorrect.append(rule)
            #######################################
            rule = 'r3d'
            ret = r3d(word, rule)
            r3drule = ret[0]
            crct = ret[1]
            if r3drule != None:
                if r3drule:
                    rule = 'r3d'
                    correct.append(rule)
                else:
                    rule = 'r3d'
                    incorrect.append(rule)
    except:
        pass
    # -----------------------------------------------
    # ----------------------RULE 4-------------------------
    try:
        if temp[-1] in DIRGHA:
            rule = 'r4a'
            r4arule = r4a(word, rule)
            if r4arule != None:
                try:
                    if r4arule:
                        rule = 'r4a'

                        correct.append(rule)
                    else:
                        rule = 'r4a'

                        incorrect.append(rule)
                except:
                    pass
    except:
        pass
        # print("###################################")
    rule = 'r4b'
    r4brule = r4b(word, rule)
    # print("###################################")
    if r4brule != None:
        try:
            if r4brule:
                rule = 'r4b'
                correct.append(rule)
            else:
                rule = 'r4b'
                incorrect.append(rule)
        except:
            pass
    # -----------------------------------------------

    # -------------------RULE 2----------------------
    try:
        if word in INVARIABLE or word in INDECLINABLE:
            rule = 'r2h'
            r2hrule = r2h(word, rule)
            if r2hrule != None:
                if r2hrule:
                    rule = 'r2h'
                    correct.append(rule)
                else:
                    rule = 'r2h'
                    incorrect.append(rule)
        # -----------------------------------------------

        else:
            # ----------------RULE 2-----------------------------
            rule = 'r2c'
            r2crule = r2c(word, rule)
            if r2crule != None:
                if r2crule:
                    rule = 'r2c'
                    correct.append(rule)
                else:
                    rule = 'r2c'
                    incorrect.append(rule)
    except:
        pass
        # print("###################################")
    rule = 'r2f'
    ls = r2f(word, rule)
    if ls != None:
        r2frule = ls[0]
        index = ls[1]
        # print(r2frule)
        if r2frule != None:
            if r2frule:
                rule = 'r2f'
                correct.append(rule)
            else:
                rule = 'r2f'
                incorrect.append(rule)
                # print(incorrect)
        # print("###################################")
        rule = 'r2e'
        ls = r2e(word, rule)
        if ls != None:
            r2erule = ls[0]
            index = ls[1]
            # print(word)
            # print(index)
            if r2erule != None:
                if r2erule:
                    rule = 'r2e'
                    correct.append(rule)
                else:
                    rule = 'r2e'
                    incorrect.append(rule)
        # print("###################################")
        rule = 'r2g'
        r2grule = r2g(word, rule)
        if r2grule != None:
            if r2grule:
                rule = 'r2g'
                correct.append(rule)
            else:
                rule = 'r2g'
                incorrect.append(rule)
        # print("###################################")

    # -----------------------------------------------
    # ---------------------RULE 5--------------------------

    try:
        if temp[-1] == VIRAMA:
            # print("# r5c RULE NOT AVAILABLE")
            rule = 'r5c'
            # print("###################################")
            # r5c

        elif temp == 'ही' or temp == 'अन':
            # print("# r5h RULE NOT AVAILABLE")
            rule = 'r5h'
            # print("###################################")
            # r5h

        else:
            rule = 'r5e'
            r5erule = r5e(word, rule)
            if r5erule:
                rule = 'r5e'
                correct.append(rule)
            else:
                # rule = "r5e: Not in DB"
                # incorrect.append(rule)
                pass
    except:
        pass
    # rule = 'r5b'
    ret = r5b(word, rule)
    if ret != None:
        r5brule = ret[0]
        crct_word_b = ret[1]
        if r5brule:
            rule = 'r5b'
            correct.append(rule)
        else:
            rule = 'r5b'
            incorrect.append(rule)

    rule = "r5f"
    ret = r5f(word, rule)
    if ret[0] != None:
        r5frule = ret[0]
        crct_word_f = ret[1]
        # print(r5frule)
        if(r5frule):
            rule = "r5f"
            correct.append(rule)
        else:
            rule = "r5f"
            incorrect.append(rule)
    # -----------------------------------------------

    # flag = 0
    # ---------------------RULE 1-------------------------
    # RULE 1a and 1c
#######################################################
    rule = 'r1a'
    r1arule = r1a(word, rule)
    if r1arule != None:
        # print("andr in r1a")
        if r1arule:
            rule = 'r1a'
            correct.append(rule)
        # else:
        #     rule = 'r1a'
        #     incorrect.append(rule)

    # print("####################################")
    rule = 'r1c'
    ls = r1c(word, rule)
    if ls != None:
        r1crule = ls[0]
        index = ls[1]

        if r1crule != None:
            if r1crule:
                rule = 'r1c'
                correct.append(rule)
            else:
                rule = 'r1c'
                incorrect.append(rule)

    ###################### Rule 1B ##########################
    rule = 'r1b'
    ls = r1b(word, rule)
    if ls != None:
        r1brule = ls[0]
        index = ls[1]
        if r1brule != None:
            if r1brule:
                rule = 'r1b'
                correct.append(rule)
            else:
                rule = 'r1b'
                incorrect.append(rule)

    ######################################################
##########################################################################################

# Driver code


def main(word, correct, incorrect, rule_dict):
    d = {}
    temp = word

    execute_others(temp, word, correct, incorrect, rule_dict)

    d["correct"] = list(set(correct))
    d["incorrect"] = list(set(incorrect))
    rule_dict[word] = d
    # print(rule_dict)
    return rule_dict
    # ---------------------------------------------------


def word_input(text, correct, incorrect):
    lst = []
    rule_dict = dict()
    lst.append(text)
    # print(lst)
    # def convert(lst):
    #     return lst[0]

    # words = convert(lst)
    accurate = []
    for word in lst:
        ret = main(word, correct, incorrect, rule_dict)
    accurate.append(ret)
    lst = []
    return (accurate)
