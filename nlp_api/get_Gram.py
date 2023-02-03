#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json

def get_Forward_Gram(word):
    forwardgrams = list()
    filePath_f = 'forward.json'
    with open(filePath_f, 'r', encoding='utf-8') as fp_f:
        forwards = dict(json.load(fp_f))
        for key, value in forwards.items():
            if key == word:
                x = list(value.keys())
                y = list(value.values())
                for a in range(len(x)):
                        if x[a] == ' ':
                            pass
                        else:
                                tup = tuple()
                                tup = x[a],y[a]
                                forwardgrams.append(tup)
    return forwardgrams


def get_Backward_Gram(word):
    backwardgrams = list()
    filePath_f = 'backward.json'
    with open(filePath_f, 'r', encoding='utf-8') as fp_f:
        backwards = dict(json.load(fp_f))
        for key, value in backwards.items():
            if key == word:
                x = list(value.keys())
                y = list(value.values())
                for a in range(len(x)):
                        if x[a] == '':
                            pass
                        else:
                            tup = tuple()
                            tup = x[a],y[a]
                            backwardgrams.append(tup)
    return backwardgrams
        

def get_Forward_Gram_next(word):
    forwardnextgrams = list()
    filePath_f = 'forwardnext.json'
    with open(filePath_f, 'r', encoding='utf-8') as fp_f:
        forwardsn = dict(json.load(fp_f))
        for key, value in forwardsn.items():
            if key == word:
                x = list(value.keys())
                y = list(value.values())
                for a in range(len(x)):
                    
                        if x[a] == '':
                            pass
                        else:
                                tup = tuple()
                                tup = x[a],y[a]
                                forwardnextgrams.append(tup)
    return forwardnextgrams

def get_Backward_Gram_previous(word):
    backwardpreviousgrams = list()
    filePath_f = 'previous.json'
    with open(filePath_f, 'r', encoding='utf-8') as fp_f:
        previous = dict(json.load(fp_f))
        for key, value in previous.items():
            if key == word:
                x = list(value.keys())
                y = list(value.values())
                for a in range(len(x)):
                        if x[a] == '':
                            pass
                        else:
                                tup = tuple()
                                tup = x[a],y[a]
                                backwardpreviousgrams.append(tup)
    return backwardpreviousgrams


def showGrams(W):
    fg = get_Forward_Gram(W)
    bg = get_Backward_Gram(W)
    fng = get_Forward_Gram_next(W)
    bpg = get_Backward_Gram_previous(W)
    return fg,bg,fng,bpg



# print(showGrams("दिग्गज"),get_Backward_Gram("दिग्गज"))



