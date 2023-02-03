###################################################################
# CONSONENTS
VELAR_CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ']
PALATAL_CONSONANTS = ['च', 'छ', 'ज', 'झ', 'ञ']
RETROFLEX_CONSONANTS = ['ट','ठ', 'ड', 'ढ', 'ण']
DENTAL_CONSONANTS = ['त', 'थ', 'द', 'ध', 'न']
LABIAL_CONSONANTS = ['प', 'फ', 'ब', 'भ', 'म']

# semi vowels in marathi
SEMI_VOWELS = ['य', 'र', 'ल', 'व']
# sibilants in marathi
SIBILANTS = ['श', 'ष', 'स']
# fricative consonant in marathi
FRIACTIVE_CONSONANTS = ['ह']
# additional consonants:
ADDITIONAL_CONSONANTS = ['ळ', 'क्ष', 'ज्ञ']

CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट','ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ळ', 'क्ष', 'ज्ञ']

###################################################################
# VOWELS
STD_VOWELS = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'ऋ',  'ॠ',  'ऌ', 'ॡ', 'अं',  'अः', 'अँ',  'ऽ' ]
DEV_VOWELS = ['ा', 'ॅ', 'ॉ', 'ि', 'ी', 'ु', 'ू', 'ॆ', 'े', 'ै', 'ॊ', 'ो', 'ौ', 'ृ', 'ॄ', 'ॢ', 'ॣ', 'ं', 'ः', '्', 'ँ' ,'ः', 'ं']

###################################################################
E = ['ई', 'ि', 'ी', 'ॆ', 'े', 'ै']
U = ['उ', 'ऊ', 'ु', 'ू']
O = ['ॊ', 'ो']

###################################################################
E_RASVA = 'इ'
E_DIRGHA = 'ई'
EE_RASVA = 'ि'
EE_DIRGHA = 'ी'

U_RASVA = 'उ'
U_DIRGHA = 'ऊ'
UU_RASVA = 'ु'
UU_DIRGHA = 'ू'

ALL_RASVA = ['इ', 'ि', 'उ', 'ु']

DIRGHA = ['ई', 'ी', 'ऊ', 'ू', 'आ', 'ा', 'े', 'ै', 'ॊ', 'ो', 'ौ', 'ओ', 'औ', 'ा', 'ॅ', 'ी', 'ॉ', 'ू', 'ॆ', 'े', 'ै', 'ॊ', 'ो', 'ौ']

ALL_RD = ['इ', 'ि', 'उ', 'ु', 'ई', 'ी', 'ऊ', 'ू']

DEV_VOWELS_T = ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ', 'ृ', 'ॄ', 'ॢ', 'ॣ', 'ं', 'ः',  'ॅ', '्',  'ँ' ]
STD_VOWELS_T = ['आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'ऋ',  'ॠ',  'ऌ', 'ॡ', 'अं',  'अः', 'अँ',  'ऽ' ,  'अँ']

# Global Variables
char_A = 'अ'
char_half = '्'

Dict_STD_DEV = dict()
for (i, j) in zip(DEV_VOWELS_T, STD_VOWELS_T):
    # print(i,j)
    Dict_STD_DEV[i] = j


# Definition Genereate SR String With Modified VOWELS
def gen_Str_SR(word):

    list_char = genList_of_char(word)
    list_SR = genSR_list(list_char)
    # initialising SR Strings
    Str_SR_O = ''
    Str_SR_M = ''

    for i in range(len(list_SR)):
        char = list_SR[i]
        if char in Dict_STD_DEV.keys():
            if i == 0:
                Str_SR_O = '' + char
                Str_SR_M = '' + Dict_STD_DEV[char]
            else:
                Str_SR_O = Str_SR_O + ' , ' + char
                Str_SR_M = Str_SR_M + ' , ' + Dict_STD_DEV[char]
        else:
            if i == 0:
                Str_SR_O = '' + char
                Str_SR_M = '' + char
            else:
                Str_SR_O = Str_SR_O + ' , ' + char
                Str_SR_M = Str_SR_M + ' , ' + char
    return Str_SR_O, Str_SR_M


# Definition list_of_char
def genList_of_char(word):
    list_char = list()
    for i in word:
        list_char.append(i)
    return list_char


# Definition Generate SR
def genSR_list(list_char):
    list_SR = list()
    for i in range(len(list_char)):
        char = list_char[i]
        if char in CONSONANTS:
            # Check immidiate next
            if i < (len(list_char) - 1) and list_char[i+1] in CONSONANTS:
                list_SR.append(char+char_half)
                list_SR.append(char_A)
            # check last char
            elif i == (len(list_char) - 1) and list_char[i] in CONSONANTS:
                list_SR.append(char+char_half)
                list_SR.append(char_A)
            else:
                list_SR.append(char)

        elif char in DEV_VOWELS or char in STD_VOWELS:
            if char == char_half and len(list_SR) != 0:
                list_SR[-1] = list_SR[-1]+char_half
            # print(list_SR)
            else:
                list_SR.append(char)

    return list_SR


# print(gen_Str_SR("अँकरच्या"))
