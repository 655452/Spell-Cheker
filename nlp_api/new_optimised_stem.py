import math
from collections import Counter
import pandas as pd
import numpy  as np
import json
from sandhiRachna import *

print_enabled = False
def similarity(myword):
    def build_vector(iterable1, iterable2):
        sandhi_iter1 = gen_Str_SR(iterable1)
        sandhi_iter2 = gen_Str_SR(iterable2)
        all_items = set()

        for i in sandhi_iter1[0].split(','):
            if i == ' ':
                continue
            all_items.add(i.strip())
        for i in sandhi_iter2[0].split(','):
            if i == ' ':
                continue
            all_items.add(i.strip())

        if print_enabled:
            # print(all_items)
            pass
        vector1 = []
        vector2 = []

        for item in all_items:
            if print_enabled:
                # print(item)
                pass
            counter = 0
            for i in sandhi_iter1[0].split(','):
                if item == i.strip():
                    counter += 1
            vector1.append(counter)

            counter = 0
            for i in sandhi_iter2[0].split(','):
                if item == i.strip():
                    counter += 1
            vector2.append(counter)
        return vector1, vector2

    def cosim(v1, v2):
        dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2))
        magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
        magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
        return dot_product / (magnitude1 * magnitude2)

    avgcs_with = []

    for onetime in range(0,1):

        json_file = 'final_dataframe.json'
        data = pd.read_json(json_file, encoding='utf-16')
        word=myword
        top5 = list()
        counter = 0

        for i in data['words']:
            if len(i) > 2 and word != i:
                if word in i or i in word:
                    top5.append(i)

        COSINE_DICT = {}
        cs = 0
        average_similarity = 0
        total_similarity = 0

        for i in top5:
            v1, v2 = build_vector(word, i)
            cs = cosim(v1, v2)

            if i not in COSINE_DICT and cs > 0.75:
                COSINE_DICT[i] = cs

        # Sorting and printing
        FINAL_DICT = {}
        COSINE_DICT = sorted(COSINE_DICT.items(), key=lambda item: item[1], reverse=True)
        for i in COSINE_DICT:
            if i not in FINAL_DICT:
                FINAL_DICT[i[0]] = i[1]

        # flush
        top5 = []
        for j in COSINE_DICT:
            if counter == 3:
                break
            counter += 1
            for i in data['words']:
                if len(i) > 2 and j[0] != i:
                    if j[0] in i:
                        top5.append(i)

        COSINE_DICT = {}
        for i in top5:
            v1, v2 = build_vector(word, i)
            cs = cosim(v1, v2)

            if i not in COSINE_DICT and cs > 0.75:
                COSINE_DICT[i] = cs

        # Sorting and printing
        COSINE_DICT = sorted(COSINE_DICT.items(), key=lambda item: item[1], reverse=True)

        for i in COSINE_DICT:
            if i not in FINAL_DICT:
                FINAL_DICT[i[0]] = i[1]

        COSINE_DICT = sorted(FINAL_DICT.items(), key=lambda item: item[1], reverse=True)

        word = []
        Cosimilarity = []
        for i in COSINE_DICT:
            # print("Cosine Similarity Value for word :", word, " : with : ",i[0], " with length ", len(i[0]) ," : is : ",i[1])
            total_similarity += i[1]
            word.append(i[0])
            Cosimilarity.append(i[1])
        if (len(COSINE_DICT)):
            avg = total_similarity / len(COSINE_DICT)
        else:
            avg = 0
        avgcs_with.append(avg)
        if cs == 0:
            # print("Cosine Similarity Value for word :", word, " is : ", cs)
            pass
        else:
            # print("")
            if (len(COSINE_DICT)):
                # print("Average Cosine Similarity :",avg)
                pass

        cslen = len(Cosimilarity)
        wlen = len(word)
        if (cslen < 10):
            for x in range(0, 10 - cslen):
                Cosimilarity.append("-")
        if (wlen < 10):
            for x in range(0, 10 - wlen):
                word.append("-")
        
        similarities = dict()
        for i in range(0,len(word)):
            similarities[word[i]] = Cosimilarity[i]
        
        Suggetions = list(similarities.keys())

        return Suggetions
		



'''
Import this module as:

from new_optimised_stem import similarity

print(similarity(word))    # gives cosine similar values in list form

'''

# print(similarity("वर्षांसाठी"))




