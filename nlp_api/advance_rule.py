import re  # regex expression
import string  # for punctuation recognition
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
#################################################################
tatsam_word = ['राजा', 'भूगोल', 'चंचू', 'पुष्प', 'परंतु', 'भगवान', 'कर', 'पशु',
               'अंध', 'जल', 'दीप', 'पृथ्वी', 'तथापि', 'कवि', 'वायु', 'भीती', 'पुत्र', 'अधापि', 'मति',
               'पुरुष', 'शिशु', 'गुरु', 'मधु', 'गंध', 'पिता', 'कन्या', 'वृक्ष', 'धर्म', 'सत्कार',
               'समर्थन', 'उत्सव', 'विद्वान', 'संत', 'निस्तेज', 'कर', 'जगन्नाथ',
               'दर्शन', 'उमेश', 'स्वामि', 'मंदिर', 'तिथी', 'सूर्य', 'स्वल्प', 'घृणा', 'पिंड', 'कलश',
               'प्रात:क', 'दंड', 'पत्र', 'ग्रंथ', 'उत्तम', 'आकाश', 'पाप', 'मंत्र', 'शिखर', 'सूत्र', 'कार्य', 'होम',
               'गणेश',
               'सभ्य', 'कन्या', 'देवर्षि', 'वृद्ध', 'संसार', 'प्रीत्यर्थ', 'कविता', 'उपकार', 'परंतु', 'गायन',
               'अश्रू', 'प्रसाद', 'अब्ज', 'राजा', 'संमती', 'घंटा', 'पुण्य', 'बुद्धी', 'अभिषेक', 'संगती', 'श्रद्धा',
               'प्रकाश',
               'सत्कार', 'देवालय', 'तारा', 'समर्थन', 'नयन', 'उत्सव', 'दुष्परिणाम', 'नैवेध', 'गुण', 'युग', 'विष',
               'प्रिय', 'मधुर', 'बहुत', 'मधुर', 'अनिल',
               'परिचित', 'स्थानिक', 'बुध', 'सुख', 'हिम', 'शिव', 'कुसुम', 'तरुण', 'रसिक', 'चतुर', 'नागरिक', 'सामाजिक',
               'पूजा', 'भीती', 'प्रीती', 'पूर्व', 'दीप', 'पीडा', 'नवीन', 'संगीत', 'लीला', 'नीती', 'कीर्ती', 'चूर्ण',
               'नीच', 'क्रीडा',
               'शरीर', 'परीक्षा']
#####################################################################################
INVARIABLE = ['परंतु', 'अध्यापि', 'तथापि', 'अति',
              'इति', 'प्रभृति', 'यध्यपि', 'नि', 'आणि']
INDECLINABLE = 'इत्यादी'
SPECIAL_WORDS = ['नागपुर', 'एखादा', 'कोणता']
######################################################################################
# CONSONANTS
VELAR_CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ']
PALATAL_CONSONANTS = ['च', 'छ', 'ज', 'झ', 'ञ']
RETROFLEX_CONSONANTS = ['ट', 'ठ', 'ड', 'ढ', 'ण']
DENTAL_CONSONANTS = ['त', 'थ', 'द', 'ध', 'न']
LABIAL_CONSONANTS = ['प', 'फ', 'ब', 'भ', 'म']
NASAL_CONSONANTS = ['ण', 'न', 'म', 'ङ']
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
######################################################################
Conjuctions = ['भर', 'विरुद्ध', 'वीण', 'उलटे', 'उलट', 'प्रत', 'प्रति', 'कडे', 'लागी', 'बद्दल', 'ऐवजी', 'जागी', 'बदली',
               'पैकी', 'पोटी', 'आतून',
               'बरोबर', 'सह', 'संगे', 'सकट', 'सहित', 'रावे', 'निशी', 'समवेत', 'विषयी', 'विशी',
               'विषयी', 'सुद्धा', 'देखील', 'ही', 'पण', 'बारीक', 'केवळ', 'फक्त', 'मात्र', 'ना',
               'पण', 'फक्त', 'केवळ', 'योग्य', 'सारखा', 'समान', 'सम', 'सयान', 'प्रमाणे',
               'बरहुकूम', 'पेक्षा', 'तर', "तम", "मध्ये", 'परीस', 'शिवाय', 'खेरीज', 'विना', "वाचून",
               'व्यक्तिरिक्त', 'परता', 'साठी', "कारणे", 'करिता', 'अथा', 'प्रीत्यर्थ', 'निमित्त', 'स्तव', 'मुळे',
               'योगे', "करून", 'कडून', 'व्दारा', 'करवी', 'हाती', 'आत', 'बाहेर', 'मागे', 'पुढे', 'मध्ये',
               'अलीकडे', 'समोर', 'जवळ', 'ठायी', 'पाशी', 'नजीक', 'पूर्वी', 'पुढे', 'आधी', 'नंतर', 'पर्यंत',
               'पावेतो', 'गतिवाचक', 'आतून', 'खालून', 'मधून', 'पर्यंत', 'पासून', 'ला', 'चे', 'ने']

############################################################################


def print_rule(word, rule):
    print("The Word is : ", word)
    print("The rule is : ", rule)
############################################################################
# जोडअक्षरातील (र)


def ruleAa3(word, rule):
    def case1(word, rule, index):
        if (word[index + 1] == 'र') or (word[index - 1] == 'र'):
            # print_rule(word, rule)
            # print('Valid Syntax according to case 1 , 2 ,and 3 e.g. राष्ट्र ,वज्र ,सर्व ')
            # print('############################################')
            return True
        else:
            return None

    def case2(word, rule, index):
        if (word[index - 1] == 'ऱ'):
            # print_rule(word, rule)
            # print('Valid Syntax according to case 4 (सुऱ्या ) र् = -')
            # print('############################################')
            return True
        elif(word[index-1] == 'र'):
            # print("Invalid syntax : Not accepted र"+'्')
            # print('############################################')
            return True
        else:
            return None

    for i in word:
        # print(i)
        try:
            if i == '्':
                index = word.index(i)
                # case1 - "ट्रंक"
                flag = case1(word, rule, index)
                if flag == True:
                    break

                # case 2 - गुऱ्हाळ
                flag = case2(word, rule, index)
                if flag == True:
                    break
        except:
            pass
############################################################################################
# जोडअक्षरातील (ह)


def ruleAa4(word, rule):
    def case(word, rule, index):
        if word[index+2] in CONSONANTS:
            # print_rule(word, rule)
            # print("Tatsam word")
            # print('############################################')
            return True
        elif word[index-1] in CONSONANTS:
            # print_rule(word, rule)
            # print("Tatbhaav")
            # print('############################################')
            return True
        else:
            return None
    for i in word:
        try:
            if i == "ह":
                index = word.index(i)
                if word[index+1] == VIRAMA:
                    case(word, rule, index)
                    # print('############################################')
        except:
            pass
############################################################################
# संयोगी (य्)


def ruleAa5(word, rule):
    for i in word:
        # print(i)
        try:
            if i == 'य':
                index = word.index(i)
                if(word[index-1] == VIRAMA):
                    # print("Valid Syntax ")
                    # print_rule(word, rule)
                    return True
            else:
                return None
        except:
            pass
#############################################################################
# पुनरुक्त अभ्यसत्य


def ruleAa6(word, rule):
    # for i in word:
    #     print(i)
    word = word.strip()
    try:
        if word.count(word[0]) == 2:
            # print_rule(word, rule)
            # print("Repetitve Word (पुनरुक्त)")
            # print('############################################')
            return [True, 1]
        elif word.count(word[-1]) == 2 and word.count(word[0]) != 2:
            # print_rule(word, rule)
            # print("Non repetetive word (अभ्यसत्य)")
            # print('############################################')
            return [True, 2]
        else:
            return None
    except:
        pass
#############################################################################
# अनुनासिक स्वराधी बिंदु द्यावा


def ruleE9(word, rule):
    try:
        if len(word) == 3 or len(word) == 4:
            if((word[-1] == 'ं') or (word[-1] == 's') or (word[-2] == 'ं')):
                # print_rule(word, rule)
                # print("valid syntax depicting nasal vowel")
                # print("#####################################################")
                return True
        else:
            return None
    except:
        pass
#####################################################
# अ चे दीर्घतव


def ruleE11(word, rule):
    # for i in word:
    #     print(i)
    # print(word[-2])
    # print(word[-1 ])
    try:
        if word[-2] in CONSONANTS and word[-1] == 'ं':
            # print("Valid Syntax: ")
            # print_rule(word, rule)
            # print('############################################')
            return True
        elif word[-1] in CONSONANTS:
            # print(f"Invalid ,there should be {'ं'} on {word[-1]}")
            word = 'correct word '+word[:]+'ं'
            # print_rule(word, rule)
            # print('############################################')
            return False
        else:
            return None
    except:
        pass
############################################################################
# अनुनसिकाकपुडे अन्यवर्गीय अनुनासिक


############################################################################
# शिरोबिंदू आणि दोन अर्थ


def ruleE13(word, rule):
    for i in word:
        # print(i)
        try:
            if i in VIRAMA:
                index = word.index(i)
                if (word[index+1] and word[index-1] in VELAR_CONSONANTS) or (word[index+1] and word[index-1] in PALATAL_CONSONANTS) or (word[index+1] and word[index-1] in LABIAL_CONSONANTS) or (word[index+1] and word[index-1] in ADDITIONAL_CONSONANTS) or (word[index+1] and word[index-1] in FRIACTIVE_CONSONANTS) or (word[index+1] and word[index-1] in DENTAL_CONSONANTS) or (word[index+1] and word[index-1] in RETROFLEX_CONSONANTS):
                    # print("Valid syntax")
                    # print_rule(word, rule)
                    return True
                else:
                    # print(
                    #     f"Invalid syntax : Consonants before and after {VIRAMA} should belong to same group")
                    # print_rule(word, rule)
                    return False
            else:
                return None
        except:
            pass
##############################################################################


def ruleU15(word, rule):
    pass
##############################################################################


def ruleU16(word, rule):
    try:
        if word[-1] in DIRGHA:
            # print("Valid Syntax")
            # print_rule(word, rule)
            # print("#############################################")
            return True
        elif len(word) == 1:
            if(any(item in word for item in DIRGHA)):
                # print("Valid Syntax")
                # print_rule(word, rule)
                # print("#############################################")
                return True
        elif(any(item in word for item in EE_DIRGHA)):
            # print("Valid Syntax")
            # print_rule(word, rule)
            # print("#############################################")
            return True
        elif(any(item in word for item in UU_DIRGHA)):
            # print("विभक्ती प्रत्यय")
            # print_rule(word, rule)
            # print("#############################################")
            return True
        else:
            # print("Check the syntax once again")
            # print_rule(word, rule)
            # print("#############################################")
            return None
    except:
        pass
##############################################################################


def ruleUU17(word, rule):
    for i in Conjuctions:
        try:
            if re.search(i, word):
                index = word.index(i)
                # print(word[index+1])
                if word[index+1] in DIRGHA:
                    # print("Valid Syntax")
                    # print_rule(word, rule)
                    pass
                    # print("#############################################")
                return [True, index]
            else:
                return None
        except:
            pass
##############################################################################


def ruleAAE22(word, rule):
    try:
        if word[-1] in DIRGHA and word[-3] in ALL_RASVA:
            # print_rule(word, rule)
            # print("Valid syntax")
            return True
        else:
            return None
    except:
        pass
##############################################################################


def ruleo29(word, rule):
    try:
        if word == 'कोणता' or word == 'एखादा':
            # print_rule(word, rule)
            # print("Valid word")
            return True
        elif word == "कोणचा" or word == 'एकादा':
            # print_rule(word, rule)
            # print("Invalid")
            if word == "कोणचा":
                # print("correct word : कोणता ")
                pass
            else:
                # print("correct word : एखादा")
                pass
            return False
        else:
            return None
    except:
        pass
##############################################################################


def main1(word, correct, incorrect, rule_dict):
    d = {}
    # word = word
    # word = 'पों'
    ###########################################################################
    rule = 'Aa3'
    Aa3 = ruleAa3(word, rule)
    if Aa3 != None:
        if Aa3:
            rule = "Aa3: Valid Syntax according to case 1 , 2 ,and 3 e.g. राष्ट्र ,वज्र ,सर्व | case 4 (सुऱ्या ) र् = -"
            correct.append(rule)
        else:
            rule = "Aa3: Invalid syntax : Not accepted र + '्'"
            incorrect.append(rule)
    #############################################################################
    rule = 'Aa4'
    Aa4 = ruleAa4(word, rule)
    if Aa4 != None:
        if Aa4:
            rule = "Aa4: Tatsam/Tatbhav words"
            correct.append(rule)
        else:
            incorrect.append(rule)
    ##############################################################################
    rule = 'Aa5'
    Aa5 = ruleAa5(word, rule)
    if Aa5 != None:
        if Aa5:
            rule = "Aa5: Valid Syntax संयोगी (य्) present"
            correct.append(rule)
        else:
            incorrect.append(rule)
    ##############################################################################
    rule = 'Aa6 '
    ls = ruleAa6(word, rule)
    if ls != None:
        Aa6 = ls[0]
        case = ls[1]
        if Aa6 and case == 1:
            rule = "Aa6: Repetitve Word (पुनरुक्त)"
            correct.append(rule)
        elif Aa6 and case == 2:
            rule = "Aa6 : Non repetetive word (अभ्यसत्य)"
        else:
            # incorrect.append(rule)
            pass
    ##############################################################################
    rule = 'E11'
    E11 = ruleE11(word, rule)
    if E11 != None:
        if E11:
            rule = "E11: Valid Syntax depicts अ चे दीर्घतव"
            correct.append(rule)
        else:
            rule = f"E11: Invalid ,there should be 'ं' on {word[-1]}"
            incorrect.append(rule)
        ##############################################################################
    rule = 'E13'
    E13 = ruleE13(word, rule)
    if E13 != None:
        if E13:
            rule = "E13: Letter in vellar consonant"
            correct.append(rule)
        else:
            rule = "E13: Invalid syntax : Consonants before and after {VIRAMA} should belong to same group"
            incorrect.append(rule)
    ##############################################################################
    rule = 'E9'
    E9 = ruleE9(word, rule)
    if E9 != None:
        if E9:
            rule = "E9: valid syntax depicting nasal vowel"
            correct.append(rule)
        else:
            # incorrect.append(rule)
            pass
    ##############################################################################
    rule = 'UU16'
    U16 = ruleU16(word, rule)
    if U16:
        rule = "UU16: consisting DIRGHA's in word"
        correct.append(rule)
    else:
        # rule = "UU16: Syntax not valid according to UU16"
        # incorrect.append(rule)
        pass
    ##############################################################################
    rule = 'UU17'
    ls = ruleUU17(word, rule)
    if ls != None:
        UU17 = ls[0]
        index = ls[1]
        try:
            if UU17:
                rule = f"UU17: consisting dirgha in {word[index+1]} "
                correct.append(rule)
            else:
                # incorrect.append(rule)
                pass
        except:
            pass
    ##############################################################################
    rule = "AAE22"
    AAE22 = ruleAAE22(word, rule)
    if AAE22 != None:
        if AAE22:
            rule = f"AAE22: Valid Syntax consisting of DIRGHA in {word[-1]} and RASVA in {word[-3]} "
            correct.append(rule)
        else:
            pass
            # incorrect.append(rule)
    ##############################################################################
    rule = 'o29'
    o29 = ruleo29(word, rule)
    if o29 != None:
        if o29:
            rule = "o29: valid word कोणता / एखादा"
            correct.append(rule)
        else:
            rule = "o29: correct word : कोणता / एखादा"
            incorrect.append(rule)

    d["correct"] = list(set(correct))
    d["incorrect"] = list(set(incorrect))
    # print(f"d:{d}")
    rule_dict[word] = d
    return rule_dict


def word_input(text, correct, incorrect):
    lst = []
    rule_dict = dict()
    lst.append(text)
    # print(lst)

    def convert(lst):
        return lst[0].split()

    accurate = []
    words = convert(lst)
    # print(words)
    for word in words:
        ret = main1(word, correct, incorrect, rule_dict)
    accurate.append(ret)
    return(accurate)
