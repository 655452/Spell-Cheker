
############################################################################################
turki_word = ['कालगी', 'बंदूक', 'कजाग']
english_word = ['टी. व्ही.', 'डॉक्टर', 'कोर्ट', 'पेन', 'पार्सल', 'सायकल', 'स्टेशन', 'हॉस्पिटल', 'बस', 'फाईल', 'रेल्वे',
                'पास', 'ब्रेक', 'कप', 'मास्तर', 'फी',
                'बॉल', 'स्टॉप', 'ऑफिस', 'एजंट', 'टेलिफोन', 'सिनेमा', 'सर्कस', 'पॅन्ट', 'बॅट', 'पोस्ट', 'तिकीट',
                'ड्राइव्हर', 'मोटर', 'कंडक्टर', 'नंबर',
                'टीचर', 'सर', 'मॅडम', 'पेपर', 'नर्स', 'पेशंट', 'इंजेक्शन', 'बटन', 'ड्रेस', 'ग्लास', 'इत्यादी']
portuges_word = ['बटाटा', 'पगार', 'बिजागरी', 'कोबी', 'हापूस', 'फणस', 'घमेले', 'पायरी', 'लोणचे', 'मेज', 'चावी', 'तुरुंग',
                 'तिजोरी', 'काडतुस', '']
farshi_word = ['रवाना', 'समान ', 'हकीकत', 'अत्तर', 'अऱ्बु', 'पेशवा', 'पोशाख', 'सौदागार', 'कामगार', 'गुन्हेगार',
               'फडणवीस', 'बाम', 'लेजीम', 'शाई', 'गरीब',
               'खानेसुमारी', 'हजार', 'शाहीर', 'मोहोर', 'सरकार', 'महिना', 'हप्ता']
arbi_word = ['अर्ज', 'इनाम', 'हुकूम', 'मेहनत', 'जाहीर', 'मंजूर', 'शाहीर', 'साहेब', 'मालक', 'मौताज', 'नक्कल', 'जबाब',
             'उर्फ', 'पैज', 'मजबूत', 'शहर', 'नजर',
             'मनोरा', 'खर्च', 'वाद', 'मदत', 'बदल']
kandi_word = ['हंडा', 'भांडे', 'अक्का', 'गाजर', 'भाकरी', 'अण्णा', 'पिशवी', 'खोली', 'बांगडी', 'लवंग', 'अडकित्ता',
              'चाकरी', 'पापड', 'खलबत्ता', 'किल्ली', 'तूप', 'चिंधी', 'गुढी', 'विळी', 'आई', 'रजई', 'तंदूर', 'चिंच',
              'खोबरे', 'कणीक', 'चिमटा', 'नथ', 'तांब्या', 'उडीद', 'गाल', 'काका', 'टाळू', 'गादी', 'खिडकी', 'गच्ची',
              'बांबू', 'ताई', 'गुंडी', 'कांबळे']
gujarati_word = ['सदरा', 'दलाल', 'ढोकळा', 'घी',
                 'डबा', 'दादर', 'रिकामटेकडा', 'ईजा', 'शेट']
hindi_word = ['बच्चा', 'बात', 'भाई', 'दिल', 'दाम', 'करोड',
              'बेटा', 'मिलाप', 'तपास', 'ऑर', 'नानी', 'मंजूर', 'ईमली']
telugu_word = ['ताळा', 'अनरसा', 'किडूकमिडूक', 'क्षिकेकाई', 'बंडी', 'डबी']
tamil_word = ['चिल्ली', 'पिल्ली', 'सार', 'मठ्ठा']
#####################################################################################
INVARIABLE = ['परंतु', 'अध्यापि', 'तथापि', 'अति',
              'इति', 'प्रभृति', 'यध्यपि', 'नि', 'आणि']
INDECLINABLE = 'इत्यादी'
# SPECIAL_WORDS = []
######################################################################################
# CONSONANTS
VELAR_CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ']
PALATAL_CONSONANTS = ['च', 'छ', 'ज', 'झ', 'ञ']
RETROFLEX_CONSONANTS = ['ट', 'ठ', 'ड', 'ढ', 'ण']
DENTAL_CONSONANTS = ['त', 'थ', 'द', 'ध', 'न']
LABIAL_CONSONANTS = ['प', 'फ', 'ब', 'भ', 'म']

# semi vowels in marathi
SEMI_VOWELS = ['य', 'र', 'ल', 'व']
# virama consonants
VIRAMA_CONSONANTS = ['य् ', 'र् ', 'ल् ', 'व् ', 'श् ', 'ष् ', 'स् ', 'ह् ']
# sibilants in marathi
SIBILANTS = ['श', 'ष', 'स']
# fricative consonant in marathi
FRIACTIVE_CONSONANTS = ['ह']
# additional consonants:
ADDITIONAL_CONSONANTS = ['ळ', 'क्ष', 'ज्ञ']

# virama
VIRAMA = '्'

CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प',
              'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ळ', 'क्ष', 'ज्ञ']

######################################################################################
# VOWELS
STD_VOWELS = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ',
              'ओ', 'औ', 'ऋ', 'ॠ', 'ऌ', 'ॡ', 'अं', 'अः', 'अँ', 'ऽ']
DEV_VOWELS = ['ा', 'ॅ', 'ॉ', 'ि', 'ी', 'ु', 'ू', 'ॆ', 'े',
              'ै', 'ॊ', 'ो', 'ौ', 'ृ', 'ॄ', 'ॢ', 'ॣ', 'ं', 'ः', '्']

######################################################################################
E = ['ई', 'ि', 'ी', 'ॆ', 'े', 'ै']
U = ['उ', 'ऊ', 'ु', 'ू']
O = ['ॊ', 'ो']

######################################################################################
E_RASVA = 'इ'
E_DIRGHA = 'ई'
EE_RASVA = 'ि'
EE_DIRGHA = 'ी'

U_RASVA = 'उ'
U_DIRGHA = 'ऊ'
UU_RASVA = 'ु'
UU_DIRGHA = 'ू'

ALL_RASVA = ['इ', 'ि', 'उ', 'ु']

DIRGHA = ['ई', 'ी', 'ऊ', 'ू', 'आ', 'ा', 'े', 'ै', 'ॊ', 'ो', 'ौ', 'ओ', 'औ', 'ा', 'ॅ', 'ी', 'ॉ', 'ू', 'ॆ', 'े', 'ै', 'ॊ',
          'ो', 'ौ']

ALL_RD = ['इ', 'ि', 'उ', 'ु', 'ई', 'ी', 'ऊ', 'ू']
#################################################################################
# Verbal prepositions
VP = ['पूर्वी', 'पुढे', 'आधी', 'नंतर', 'पर्यंत', 'पावेतो',
      'गतिवाचक', 'आतून', 'खालून', 'मधून', 'पर्यंत',
      'पासून', 'आत', 'बाहेर', 'मागे', 'पुढे', 'मध्ये',
      'अलीकडे', 'समोर', 'जवळ', 'ठायी', 'पाशी',
      'नजीक', 'मुळे', 'योगे', 'करून', 'कडून',
      'व्दारा', 'करवी', 'हाती', 'साठी', 'कारणे',
      'करिता', 'अथा', 'प्रीत्यर्थ', 'निमित्त', 'स्तव',
      'शिवाय', 'खेरीज', 'विना', 'वाचून', 'व्यक्तिरिक्त', 'परता', 'पेक्षा', 'तर', 'तम', 'मध्ये', 'परीस', 'योग्य', 'सारखा', 'समान',
      'सम', 'सयान', 'प्रमाणे', 'बरहुकूम', 'मात्र', 'ना', 'पण', 'फक्त', 'केवळ',
      'सुद्धा', 'देखील', 'ही', 'पण', 'बारीक', 'केवळ', 'फक्त',
      'विषयी', 'विशी', 'विषयी', 'बरोबर', 'सह', 'संगे', 'सकट', 'सहित', 'रावे', 'निशी', 'समवेत',
      'पैकी', 'पोटी', 'आतून', 'बद्दल', 'ऐवजी', 'जागी', 'बदली', 'प्रत', 'प्रति', 'कडे', 'लागी',
      'विरुद्ध', 'वीण', 'उलटे', 'उलट', 'भर']


#################################################################################
# Inflectional suffix
IS = ['स', 'ला', 'ते', 'ना', 'चा', 'ची', 'चे',
      'च्या', 'ने', 'ऐ', 'शी', 'ही', 'ऊन', 'हून', 'त', 'ई', 'आ', 'नो']


#################################################################################
print("-----------------RULES---------------------")

#


def print_rule(word, rule):
    return [word, rule]
    # print("The Word is : ", word)
    # print("The rule is : ", rule)


######################################################################################
# RULE 1 CORECT WORD FROMER:


def correct_word(word, resp):
    try:
        if word[1] == 'ू' or word[1] == 'ु' or word[1] == 'ी' or word[0] == 'ि':
            if resp:
                word1 = word[0:2] + 'ं' + word[2:]
                return word1

            else:
                word1 = word[0:-1] + 'ं' + word[-1]
                return word1
        else:
            if resp:
                word1 = word[0]+'ं'+word[1:]
                return word1
            else:
                word1 = word[0:-1]+'ं'+word[-1]
                return word1
    except:
        pass
######################################################################################


def r1a(word, rule):
    word = word.strip()
    for x in word:
        print(x, end=" ")
    try:
        if (word[0] not in SEMI_VOWELS and word[0] not in SIBILANTS and word[0] not in FRIACTIVE_CONSONANTS) and (word[-1] not in SEMI_VOWELS and word[-1] not in SIBILANTS and word[-1] not in FRIACTIVE_CONSONANTS):
            if 'ं' in word:
                # print_rule(word, rule)
                return True
                # print("valid syntax")
                # print("It is a clear Nasal pronounciation")
            else:
                if(word[-1] in DIRGHA):
                    resp = True
                    # print_rule(word, rule)
                    # print("invalid syntax::[ ", word[0],
                    #       " ] A letter has an ANUSVARA above it.")
                    # print("CORRECT WORD : ", correct_word(word, resp))
                    # print("it is not nasal pronouncation")
                    return False
                else:
                    resp = False
                    # print_rule(word, rule)
                    # print("invalid syntax::[ ", word[-2],
                    #       " ] A letter has an ANUSVARA above it.")
                    # print("CORRECT WORD : ", correct_word(word, resp))
                    # print("it is not nasal pronouncation")
                    return False
        else:
            return None
    except:
        pass

##########################################################################
# RULE 1 : c


def r1c(word, rule):
    word = word.strip()
    for x in word:
        try:
            if x in SEMI_VOWELS or x in SIBILANTS or x in FRIACTIVE_CONSONANTS or x in VIRAMA:
                if x == word[0]:
                    continue
                else:
                    index = word.index(x)
                    if word[1] == "ं":
                        # print_rule(word, rule)
                        # print("valid syntax")
                        return [True, None]
                    elif word[index - 1] == "ं":
                        print_rule(word, rule)
                        # print("valid syntax")
                        return [True, None]
                    else:
                        if (any(item in word for item in "ं")):
                            print_rule(word, rule)
                            # print("VALID")
                            return [True, None]
                        else:
                            print_rule(word, rule)
                            # print("invalid  syntax::[", word[1], " ] or [ ", word[index - 1],
                            #       " ] should have ANUSVARA above or after it respectively.")
                            return [False, index]
            else:
                return None
        except:
            pass
# Rule 1 : d

# use of stemmer comes in play


# def r1d(word, rule):
#    word = word.strip()
 #   if any(item in IS for item in word[-1]) or if any(item in VP for item in word):

        ###########################################################################################
"""
Rule 2 :
    sub rule 1 ::  follows
    sub rule 2 ::  follows
    sub rule 3 ::  follows
    sub rule 4 ::  follows
    sub rule 5 ::  Sanskrit Exception
    sub rule 6 ::  Almost follows
    sub rule 7 ::  Almost follows
    sub rule 8 ::  Sanskrit Exception

"""


######################################################################################
# rule 2a
def r2a(word, rule):
    word = word.strip()
    try:
        if len(word) == 2:
            if word[-1] == EE_RASVA:
                # print_rule(word, rule)
                # print("Invalid Synatx :: [ ", word[-1],
                #       " ] Make it EE_DIRGHA [ ", EE_DIRGHA, " ]")
                return False

            elif word[-1] == UU_RASVA:
                # print_rule(word, rule)
                # print("Invalid Synatx :: [ ", word[-1],
                #       " ] Make it UU_DIRGHA [ ", EE_DIRGHA, " ]")
                return False

            else:
                # print_rule(word, rule)
                # print("Valid Syntax")
                return True
        else:
            return None
    except:
        pass
######################################################################################
# rule 2b


def r2b(word, rule):
    word = word.strip()
    # l = word[-1]
    # print(l)
    print_rule(word, rule)
    try:
        if word[-1] == E_RASVA:
            # # print_rule(word, rule)
            # print("Invalid Syntax :: [ ", word[-1],
            #       " ] E_RASVA change it to E_DIRGHA [ ", E_DIRGHA, " ]")
            return False

        elif word[-1] == EE_RASVA:
            # print_rule(word, rule)
            # print("Invalid Syntax :: [ ", word[-1],
            #       " ] EE_RASVA change it to EE_DIRGHA [ ", EE_DIRGHA, " ]")
            return False

        elif word[-1] == U_RASVA:
            # print_rule(word, rule)
            # print("Invalid Syntax :: [ ", word[-1],
            #       " ] U_RASVA change it to U_DIRGHA [ ", U_DIRGHA, " ]")
            return False

        elif word[-1] == UU_RASVA:
            # print_rule(word, rule)
            # print("Invalid Synatx :: [ ", word[-1],
            #       " ] UU_RASVA change it to UU_DIRGHA [ ", UU_DIRGHA, " ]")
            return False
        else:
            # print("Valid Synatx")
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
    print_rule(word, rule)
    try:
        if word[-1] == EE_RASVA:
            # print("Invalid Syntax :: [ ", word[-1],
            #       " ] Make it EE_DIRGHA [ ", EE_DIRGHA, " ]")
            return False

        elif word[-1] == UU_RASVA:
            # print("Invalid Syntax :: [ ", word[-1],
            #       " ] Make it UU_DIRGHA [ ", UU_DIRGHA, " ]")
            return False

        else:
            # print("Valid Syntax")
            return True
    except:
        pass
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
    for x in word:
        try:
            if x == EE_RASVA or x == UU_RASVA:
                print_rule(word, rule)
                # print('Valid Syntax')
                return [True, None]
            if x == EE_DIRGHA:
                print_rule(word, rule)
                index = word.index(x)
                # print("Invalid Syntax :: [ ", word[index],
                #       " ] Make it EE_RASVA [ ", EE_RASVA, " ]")
                # break
                return [False, index]
            elif x == UU_DIRGHA:
                print_rule(word, rule)
                index = word.index(x)
                # print("Invalid Syntax :: [ ", word[index],
                #       " ] Make it UU_RASVA [ ", UU_RASVA, " ]")
                # break
                return [False, index]
            else:
                return None
        except:
            pass
# r2e(word="मृत्यूलेख")
################################################################
# words_example = ['गुरूदक्षिणा','वायुपुत्रा',''मृत्युलेख','भानूविलास','गतिमान','हरिकृपा']
################################################################

# RULE 2 : f
# First Syllable in compound word contain long vowel , then let it long vowel
#######################################################################


def r2f(word, rule):
    word = word.strip()
    for x in word:
        try:
            if x == EE_DIRGHA or x == UU_DIRGHA:
                print_rule(word, rule)
                # print("Valid Syntax")
                # break
                index = 1
                return [True, index]

            if x == EE_RASVA:
                print_rule(word, rule)
                index = word.index(x)
                # print("Invalid Syntax :: [ ", word[index],
                #       " ] Make it EE_DIRGHA [ ", EE_DIRGHA, " ]")
                # break
                return [False, index]

            elif x == UU_RASVA:
                print_rule(word, rule)
                index = word.index(x)
                # print("Invalid Syntax :: [ ", word[index],
                #       " ] Make it UU_DIRGHA [ ", UU_DIRGHA, " ]")
                # break
                return [False, index]
            else:
                return None
        except:
            pass
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
        if VIRAMA in word[-1]:
            print_rule(word, rule)
            # print("Convert EE_RASVA [ ", EE_RASVA, " ] to EE_DIRGHA [ ",
            #       EE_DIRGHA, " ] and remove न् in word", word)
            return True
        else:
            return None
    except:
        pass
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
    # print_rule(word, rule)
    try:
        if word[-1] not in DEV_VOWELS:
            if word[-2] == E_RASVA:
                # print_rule(word, rule)
                # print("Invalid Syntax :: [ ", word[-2],
                #       " ] E_RASVA change it to E_DIRGHA [ ", E_DIRGHA, " ]")
                # print(
                #     "If the word in tatsam it remain as same as in Sanskrit under in rule r3b please ignore above condition")
                return False

            elif word[-2] == EE_RASVA:
                # print_rule(word, rule)
                # print("Invalid Synatx :: [ ", word[-2],
                #       " ] EE_RASVA change it to EE_DIRGHA [ ", EE_DIRGHA, " ]")
                # print(
                #     "If the word in tatsam it remain as same as in Sanskrit under in rule r3b please ignore above condition")
                return False

            elif word[-2] == U_RASVA:
                # print_rule(word, rule)
                # print("Invalid Syntax :: [ ", word[-2],
                #       " ] U_RASVA change it to U_DIRGHA [ ", U_DIRGHA, " ]")
                # print(
                #     "If the word in tatsam it remain as same as in Sanskrit under in rule r3b please ignore above condition")
                return False

            elif word[-2] == UU_RASVA:
                # print_rule(word, rule)
                # print("Invalid Synatx :: [ ", word[-2],
                #       " ] UU_RASVA change it to UU_DIRGHA [ ", UU_DIRGHA, " ]")
                # print(
                #     "If the word in tatsam it remain as same as in Sanskrit under in rule r3b please ignore above condition")
                return False

            else:
                # print_rule(word, rule)
                # print("Valid Synatx")
                return True
    except:
        pass
######################################################################################
# rule 3b


def r3b(word, rule):
    # word = word.strip()
    # print(f'rule {rule} not available')
    return None


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
                    # print(
                    #     "Invalid Syntax :: [ ", word[-3], " ] Upantya E_DIRGHA change it to E_RASVA [ ", E_RASVA, " ]")
                    # print(
                    #     "If the word in tatsam it remain as same as in Sanskrit under in rule r3d please ignore above condition")
                    return False

                elif word[-3] == EE_DIRGHA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Syntax :: [ ", word[-3], " ] Upantya EE_DIRGHA change it to EE_RASVA [ ", EE_RASVA, " ]")
                    # print(
                    #     "If the word in tatsam it remain as same as in Sanskrit under in rule r3d please ignore above condition")
                    return False

                elif word[-3] == U_DIRGHA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Synatx :: [ ", word[-3], " ] Upantya U_DIRGHA change it to U_RASVA [ ", U_RASVA, " ]")
                    # print(
                    #     "If the word in tatsam it remain as same as in Sanskrit under in rule r3d please ignore above condition")
                    return False

                elif word[-3] == UU_DIRGHA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Synatx :: [ ", word[-3], " ] Upantya UU_DIRGHA change it to UU_RASVA [ ", UU_RASVA, " ]")
                    # print(
                    #     "If the word in tatsam it remain as same as in Sanskrit under in rule r3d please ignore above condition")
                    return False
                else:
                    print_rule(word, rule)
                    # print("Valid Synatx")
                    return True
        else:
            return None
    except:
        pass
###########################################################################################


def r4a(word, rule):
    word = word.strip()
    try:
        if len(word) > 2:
            if word[-1] in DIRGH:
                print_rule(word, rule)
                if word[-3] == E_RASVA:
                    # print(
                    #     "Invalid Syntax :: [ ", word[-3], " ] Upantya E_RASVA change it to EE_DIRGHA [ ", EE_DIRGHA, " ]")
                    return False

                elif word[-3] == EE_RASVA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Syntax :: [ ", word[-3], " ] Upantya E_RASVA change it to EE_DIRGHA [ ", EE_DIRGHA, " ]")
                    return False

                elif word[-3] == U_RASVA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Syntax :: [ ", word[-3], " ] Upantya U_RASVA change it to UU_DIRGHA [ ", UU_DIRGHA, " ]")
                    return False

                elif word[-3] == UU_RASVA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Syntax :: [ ", word[-3], " ] Upantya UU_RASVA change it to UU_DIRGHA [ ", UU_DIRGHA, " ]")
                    return False
                else:
                    print_rule(word, rule)
                    # print("Valid Synatx")
                    return True
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
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Synatx :: [ ", word[-3], " ] Upantya E_DIRGHA change it to EE_RASVA [ ", EE_RASVA, " ]")
                    # print(
                    #     "If the word in tatsam it remain as same as in Sanskrit under in rule r4c please ignore above condition")
                    return False

                elif word[-3] == EE_DIRGHA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Synatx :: [ ", word[-3], " ] Upantya E_DIRGHA change it to EE_RASVA [ ", EE_RASVA, " ]")
                    # print(
                    #     "If the word in tatsam it remain as same as in Sanskrit under in rule r4c please ignore above condition")
                    return False

                elif word[-3] == U_DIRGHA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Synatx :: [ ", word[-3], " ] Upantya U_DIRGHA change it to UU_RASVA [ ", UU_RASVA, " ]")
                    # print(
                    #     "If the word in tatsam it remain as same as in Sanskrit under in rule r4c please ignore above condition")
                    return False

                elif word[-3] == UU_DIRGHA:
                    print_rule(word, rule)
                    # print(
                    #     "Invalid Synatx :: [ ", word[-3], " ] Upantya UU_DIRGHA change it to UU_RASVA [ ", UU_RASVA, " ]")
                    # print(
                    #     "If the word in tatsam it remain as same as in Sanskrit under in rule r4c please ignore above condition")
                    return False
                else:
                    print_rule(word, rule)
                    # print("Valid Synatx")
                    return True
            else:
                return None
    except:
        pass
#########################################################################################
# RULE 5 : e


def r5e(word, rule):
    word = word.strip()
    try:
        if word in turki_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in english_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in portuges_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in farshi_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in arbi_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in kandi_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in gujarati_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in hindi_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in telugu_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        elif word in tamil_word:
            print_rule(word, rule)
            # print("valid syntax")
            return True
        else:
            return False
    except:
        pass

#########################################################################################


# Driver code
def main(word, correct, incorrect, rule_dict):
    d = {}
    temp = word

    def execute_others():
        x_list = []
        for x in temp:
            if x in ALL_RD:
                x_list.append(x)

        # ----------------RULE 2-----------------------------
        if len(temp) < 3 and any(item in x_list for item in DEV_VOWELS):
            rule = 'r2a'
            r2arule = r2a(word, rule)
            if r2arule != None:
                # print("###################################")
                if r2arule:
                    rule = "r2a : Valid Syntax contains proper DIRGHAS"
                    correct.append(rule)
                else:
                    rule = f"r2a : Invalid Synatx :: {word[-1]} Make it EE_DIRGHA/UU_DIRGHA {EE_DIRGHA}/{UU_DIRGHA}"
                    incorrect.append(rule)

        if word[-1] in ALL_RD and any(item in x_list for item in DEV_VOWELS) or any(item in x_list for item in STD_VOWELS):
            rule = 'r2b'
            r2brule = r2b(word, rule)
            # print("###################################")
            if r2brule:
                rule = "r2b : Valid Syntax contains proper DIRGHAS"
                correct.append(rule)
            else:
                rule = f"r2b: Invalid Syntax:: {word[-1]} E_RASVA/EE_RASVA/U_RASVA/UU_RASVA change it to E_DIRGHA {E_DIRGHA}/{EE_DIRGHA}/{U_DIRGHA}/{UU_DIRGHA}"
                incorrect.append(rule)
        # ---------------------RULE 3--------------------------
        if temp[-1] in CONSONANTS:
            rule = 'r3a'
            r3arule = r3a(word, rule)
            if r3arule:
                rule = "r3a: Valid Syntax contains proper DIRGHAS"
                correct.append(rule)
            else:
                rule = f"""r3a: Invalid Syntax :: {word[-2]} E_RASVA/EE_RASVA/UU_RASVA/U_RASVA change it to E_DIRGHA/EE_DIRGHA/U_DIRGHA/UU_DIRGHA {E_DIRGHA}/{EE_DIRGHA}/{U_RASVA}/{UU_RASVA}.If word is tatsam leave as it is !!"""
                incorrect.append(rule)
            # print("###################################")
            rule = 'r3b'
            r3brule = r3b(word, rule)
            # print("###################################")
            if r3brule != None:
                if r3brule:
                    rule = "r3b: Valid Syntax"
                    correct.append(rule)
                else:
                    incorrect.append(rule)
        try:
            if temp[-2] in CONSONANTS and any(item in x_list for item in DIRGHA):
                rule = 'r3c'
                r3crule = r3c(word, rule)
                # r3d(word)
                if r3crule != None:
                    if r3crule:
                        rule = "r3c: Valid Syntax consisting Upantya RASVAS"
                        correct.append(rule)
                    else:
                        rule = f"""r3c: Invalid Syntax :: {word[-3]} Upantya E_DIRGHA/EE_DIRGHA/U_DIRGHA/UU_DIRGHA change it to E_RASVA/EE_RASVA/U_RASVA/UU_RASVA {E_RASVA}/{EE_RASVA}/{U_RASVA}/{UU_RASVA}.
                    """
                        incorrect.append(rule)
        except:
            pass
        # -----------------------------------------------
        # ----------------------RULE 4-------------------------
        if temp[-1] in DIRGHA:
            rule = 'r4a'
            r4arule = r4a(word, rule)
            if r4arule != None:
                try:
                    if r4arule:
                        rule = "r4a:Valid Syntax containing Upantya RASVAS"
                        correct.append(rule)
                    else:
                        rule = f"""r4a: Invalid Syntax :: {word[-3]} Upantya E_RASVA/EE_RASVA/U_RASVA/UU_RASVA change it to EE_DIRGHA/E_DIRGHA/U_RASVA/UU_RASVA {EE_DIRGHA}/{E_DIRGHA}/{U_RASVA}/{UU_RASVA}"""
                        incorrect.append(rule)
                except:
                    pass
            # print("###################################")
            rule = 'r4b'
            r4brule = r4b(word, rule)
            # print("###################################")
            if r4brule != None:
                try:
                    if r4brule:
                        rule = "r4b: Valid Syntax consist proper RASVAS"
                        correct.append(rule)
                    else:
                        rule = f"""r4a: Invalid Syntax :: {word[-3]} Upantya E_DIRGHA/EE_DIRGHA/U_DIRGHA/UU_DIRGHA change it to EE_RASVA/E_RASVA/U_RASVA/UU_RASVA {EE_DIRGHA}/{E_DIRGHA}/{U_RASVA}/{UU_RASVA}"""
                        incorrect.append(rule)
                except:
                    pass
        # -----------------------------------------------

        # -------------------RULE 2----------------------
        if word in INVARIABLE or word in INDECLINABLE:
            rule = 'r2h'
            r2hrule = r2h(word, rule)
            if r2hrule != None:
                if r2hrule:
                    rule = "r2h: Word is INVARIABLE or INDECLINABLE"
                    correct.append(rule)
                else:
                    rule = f"""r2h: INVALID SYNTAX!! INVARIBALE ,{INVARIABLE},witten ending with short vowels | "INDECLINABLE {INDECLINABLE} written in long vowel"""
                    incorrect.append(rule)
         # -----------------------------------------------

        else:
            # ----------------RULE 2-----------------------------
            rule = 'r2c'
            r2crule = r2c(word, rule)
            if r2c:
                rule = "r2c: Valid Syntax contains DIRGHAS"
                correct.append(rule)
            else:
                rule = f"r2c: Invalid Syntax :: {word[-1]} Make it EE_DIRGHA/UU_DIRGHA {EE_DIRGHA}/{UU_DIRGHA}"
                incorrect.append(rule)
            # print("###################################")
            rule = 'r2f'
            ls = r2f(word, rule)
            if ls != None:
                r2frule = ls[0]
                index = ls[1]
                if r2frule:
                    rule = "r2f:Valid Syntax first syllable contains long vowel"
                    correct.append(rule)
                else:
                    rule = f"r2c: Invalid Syntax :: {word[index]} Make it EE_DIRGHA/UU_DIRGHA {EE_DIRGHA}/{UU_DIRGHA}"
                    incorrect.append(rule)
            # print("###################################")
            rule = 'r2e'
            ls = r2e(word, rule)
            if ls != None:
                r2erule = ls[0]
                index = ls[1]
                if r2erule:
                    rule = "r2e: Valid Syntax contains RASVA"
                    correct.append(rule)
                else:
                    rule = f"r2e: Invalid Syntax:: {word[index]} Make it EE_RASVA/UU_RASVA {EE_RASVA}/{UU_RASVA}"
                    incorrect.append(rule)
            # print("###################################")
            rule = 'r2g'
            r2grule = r2g(word, rule)
            if r2grule != None:
                if r2grule:
                    rule = f"r2g: Convert EE_RASVA {EE_RASVA} to EE_DIRGHA {EE_DIRGHA} and remove न् in word {word}"
                    correct.append(rule)
                else:
                    rule = "r2g: Not applicable"
                    incorrect.append(rule)
            # print("###################################")

        # -----------------------------------------------
        # ---------------------RULE 5--------------------------

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
                rule = "r5e: Valid Syntax"
                correct.append(rule)
            else:
                # rule = "r5e: Not in DB"
                # incorrect.append(rule)
                pass
        # -----------------------------------------------

    flag = 0
    # ---------------------RULE 1-------------------------
    for x in temp:
        if x == 'ं':
            flag = 1
            break
        else:
            flag = 0
            continue

    # RULE 1a and 1c
    if (flag == 1):
        if 'ं' in word and any(item in word for item in ALL_RD):
            execute_others()
        else:
            rule = 'r1a'
            r1arule = r1a(word, rule)
            if r1arule != None:
                if r1arule:
                    rule = "r1a : Clear nasal pronounciation"
                    correct.append(rule)
                else:
                    rule = "r1a : Unclear nasal pronounciation"
                    incorrect.append(rule)

            # print("####################################")
            rule = 'r1c'
            ls = r1c(word, rule)
            if ls != None:
                r1crule = ls[0]
                index = ls[1]
                if r1crule:
                    rule = "r1c: Consist semi-vowels,sibilants and friactive consonants"
                    correct.append(rule)
                else:
                    rule = f"r1c: {word[1]}  or  {word[index - 1]} should have ANUSVARA above or after it respectively."
                    incorrect.append(rule)

    else:
        execute_others()

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

    def convert(lst):
        return lst[0].split()

    words = convert(lst)
    accurate = []
    for word in words:
        ret = main(word, correct, incorrect, rule_dict)
    accurate.append(ret)
    return (accurate)
