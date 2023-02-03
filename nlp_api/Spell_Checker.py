import json
from MED import *
import csv
from new_optimised_stem import *

with open("Words.txt", "r", encoding='UTF-16') as F:
    folist = list(F.read().split(","))

def CheckSpell(Word):
    # if Word in folist:
    #     return ["Black"]
    # else:
        OP = similarity(Word)
        return OP[:5]

def Add_To_Dictionary(Word):
    with open("Words.txt","a", encoding='UTF-8') as F:
        F.write(Word + ",")



# print(CheckSpell("वईट")[0])



# पाहण्‍साठी



