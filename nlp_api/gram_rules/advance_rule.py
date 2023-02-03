import re  # regex expression
# import string  # for punctuation recognition
from . import hardcode
from basic_rule import r1a
from .variables import *
############################################################################


# def print_rule(word, rule):
#     print("The Word is : ", word)
#     print("The rule is : ", rule)
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
        if word[index - 1] == 'ऱ':
            # print_rule(word, rule)
            # print('Valid Syntax according to case 4 (सुऱ्या ) र् = -')
            # print('############################################')
            return True
        elif word[index - 1] == 'र':
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
            return True
        elif word[index-1] in CONSONANTS:
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
    try:
        if (word[-2] in CONSONANTS) and (word[-1] == 'ं'):
            return True
        elif (word[-1] in CONSONANTS) and (word[-2] == 'ं'):
            return True
        elif (word[-1] in CONSONANTS) or (word[-2] in CONSONANTS) or (word[-3] in CONSONANTS) or (word[1] in CONSONANTS):
            # new_word = 'correct word '+word[:]+'ं'
            return False
        else:
            return None
    except:
        return None
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
        if word[-1] in EE_DIRGHA or word[-1] in UU_DIRGHA:
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
            return False
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
            rule = 'Aa3'
            correct.append(rule)
        else:
            rule = 'Aa3'
            incorrect.append(rule)
    #############################################################################
    rule = 'Aa4'
    Aa4 = ruleAa4(word, rule)
    if Aa4 != None:
        if Aa4:
            rule = 'Aa4'
            correct.append(rule)
        else:
            rule = 'Aa4'
            incorrect.append(rule)
    ##############################################################################
    rule = 'Aa5'
    Aa5 = ruleAa5(word, rule)
    if Aa5 != None:
        if Aa5:
            rule = 'Aa5'
            correct.append(rule)
        else:
            rule = 'Aa5'
            incorrect.append(rule)
    ##############################################################################
    rule = 'Aa6 '
    ls = ruleAa6(word, rule)
    if ls != None:
        Aa6 = ls[0]
        case = ls[1]
        if Aa6 and case == 1:
            rule = "Aa6"
            correct.append(rule)
        elif Aa6 and case == 2:
            rule = "Aa6"
        else:
            # incorrect.append(rule)
            pass
    ##############################################################################
    rule = 'E11'
    E11 = ruleE11(word, rule)
    # print(f"BG {r1a(word, 'r1a')}")
    if r1a(word, "r1a") != True:
        if E11:
            rule = 'E11'
            correct.append(rule)
        # else:
        #     rule = 'E11'
        #     incorrect.append(rule)
        ##############################################################################
    rule = 'E13'
    E13 = ruleE13(word, rule)
    if E13 != None:
        if E13:
            rule = 'E13'
            correct.append(rule)
        else:
            rule = 'E13'
            incorrect.append(rule)
    ##############################################################################
    rule = 'E9'
    E9 = ruleE9(word, rule)
    if E9 != None:
        if E9:
            rule = 'E9'
            correct.append(rule)
        else:
            # incorrect.append(rule)
            pass
    ##############################################################################
    rule = 'UU16'
    U16 = ruleU16(word, rule)
    if U16:
        rule = 'UU16'
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
                rule = 'UU17'
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
            rule = "AAE22"
            correct.append(rule)
        else:
            pass
            # incorrect.append(rule)
    ##############################################################################
    rule = 'o29'
    o29 = ruleo29(word, rule)
    if o29 != None:
        if o29:
            rule = 'o29'
            correct.append(rule)
        else:
            rule = 'o29'
            incorrect.append(rule)
    ##############################################################################
    rule = "AA1"
    flag, AA1 = hardcode.AA1(word)
    flag_a, crct_word = hardcode.db_dict_word(word)
    if flag:
        rule = "AA1"
        incorrect.append(rule)
    if crct_word != None:
        if flag_a:
            rule = "AA1"
            correct.append(rule)
        else:
            rule = "AA1"
            incorrect.append(rule)

    ###############################################################################
    ###############################################################################
    d["correct"] = list(set(correct))
    d["incorrect"] = list(set(incorrect))
    rule_dict[word] = d
    return rule_dict


def word_input(text, correct, incorrect):
    lst = []
    rule_dict = dict()
    lst.append(text)
    # print(lst)

    # def convert(lst):
    #     return lst[0]

    accurate = []
    # words = convert(lst)
    # print(words)
    for word in lst:
        ret = main1(word, correct, incorrect, rule_dict)
    accurate.append(ret)
    return(accurate)
