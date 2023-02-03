import csv
import json
import csv
import numpy as np
import pandas as pd

folist=[]
'''
with open ('final_dataframe.json', 'r', encoding="UTF-16") as J:
    data = dict(json.load(J))
    folist = data['words']
'''
columns = ['word','count','str_sandhi_rachana']
df = pd.read_csv('MED.csv', usecols=columns)
for w in df['word']:
    folist.append(w)



#LEVENSHTIEN ALGORITHM
def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix, matrix[size_x - 1, size_y - 1])


#THE MINIMUM EDIT DISTANCE FUNCTION
def minEditDistance(matrix, seq1, seq2):
  size_x, size_y = matrix.shape
  x = size_x-1
  y = size_y-1
  while x<=size_x and x>0 and y<=size_y and y>0:
    

    min_value = min(matrix[x-1,y], matrix[x-1,y-1], matrix[x,y-1])
    if matrix[x-1,y-1] == min_value:
      if matrix[x-1, y-1] == matrix[x,y]:
        x = x-1
        y = y-1

      elif matrix[x-1, y-1] == matrix[x,y] -1 :
       
        x = x-1   

        y = y-1

    elif matrix[x-1, y] == min_value:
      if matrix[x-1, y] == matrix[x,y] -1:
        
        x = x-1
        y = y
      
    elif matrix[x, y-1] == min_value:
      if matrix[x, y-1] == matrix[x,y] -1:
        
        x = x
        y = y-1

    
  return(x,y)

#FUNCTION TO CALCULATE MINIMUM EDIT DISTANCE OF RANDOM 100 WORDS WHEN THEY ARE IN DATABASE
def main1(seq2):
  cou = 0
  dictSortedMinEditDistance = dict()
  ### Read csv file
  #filePath_R = 'fodata.csv'
  #with open(filePath_R , newline='', encoding='UTF-8') as csvRFile:
    # csvDictReader = csv.DictReader(csvRFile)
  for p in folist:
      seq1 = word = p   
      seq2 = seq2
      matrix, x_1 = levenshtein(seq1, seq2)
      r = minEditDistance(matrix, seq1, seq2)
      dictSortedMinEditDistance[word] = int(x_1)
  tenDictSortedMinEditDistance = list()
  tenDictSortedMinEditDistance = sorted(dictSortedMinEditDistance.items(), key = lambda x : x[1])
  return tenDictSortedMinEditDistance[:5]

#give word input to main1 and get 5 closest words
