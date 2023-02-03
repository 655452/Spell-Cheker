# from Spell_Checker import *
# Text=" दिग्गजही  दिग्गजही दिग्गजही दिग्गही"  

# TEXTL = Text.split()
# TextD=[]
# x=0
# for i in TEXTL:
#     if i in folist:
#         i=[1,i]
#         TextD.append(i)
#         x+=1
#         print(type(i))
#     else:
#         i=[0,i]
        
#         TextD.append(i)
#         x+=1
#         print(False)

# print(TextD)
# y=0
# for i in TextD:
#     print(i[1])
#     y+=y

# secon Api part

# import requests
# import json
# BASE="http://127.0.0.1:5000/"
# data="दिग्गजही"
# payload={"Word":data}
# response=requests.post(BASE+"parse_word",json=payload)
# obj=response.json()
# # print(response.json())
# print(obj)

# {'Correct_Rules': ['UU16', 'r3c', 'r2b', 'r2e'], 'Incorrect_Rules': ['r2c', 'r2f'], 'Result': 1, 
# 'Spell': ['दिग्गजही', 'दिग्गज', 'गजही', 'दिग्गजांवरील', 'दिग्गजांचीही']}
# {'data':
#  {'Spell': 
#     ['दिग्गजही', 'दिग्गज', 'गजही', 'दिग्गजांवरील', 'दिग्गजांचीही'], 
#     'Correct_Rulespy': 
#     ['UU16', 'r2e', 'r3c', 'r2b'], 
#     'Incorrect_Rules': 
#     ['r2f', 'r2c'], 
#       'Result': 1
#     }
#     }



# arr=[
# {'Correct_Rules': ['r1c', 'r1b', 'r2e'], 'Incorrect_Rules': ['r2f', 'r2c'], 'Result': 1, 'Spell': ['दिग्गज्जांसोबत', 'दिग्गजांसोबत', 'दिग्गजांत', 'दिग्गजांसोबतची', 'दिग्गजांसोबतच्या']}, 
# {'Correct_Rules': ['r2e'], 'Incorrect_Rules': ['r2f', 'r2c'], 'Result': 0, 'Spell': ['दिग्गजांसह', 'गजासह', 'दिग्गजांसमोर', 'दिग्गजांसमवेत', 'दिग्गजांवर']}, 
# {'Correct_Rules': ['r1c', 'r1b', 'r1a', 'r2e'], 'Incorrect_Rules': ['r2f', 'r2c'], 'Result': 1, 'Spell': ['दिग्गजांवर', 'गदिमांवर', 'अजितदादांवर', 'गजांवर', 'अंदाजांवर']}, 
# {'Correct_Rules': ['r2e'], 'Incorrect_Rules': ['r2f', 'r2c'], 'Result': 0, 'Spell': ['दिग्ग्ज', 'दिग्गज', 'दिग्गन', 'दिग्गजही', 'दिग्गजांत']}
# ]

# # print(arr[1]['Correct_Rules'])
# for i in range(0,len(arr)):
#     print("Incorrect Rules:")
#     for j in arr[i]['Correct_Rules']:
#         print(j)
#     print("correct Rules:")
#     for j in arr[i]['Incorrect_Rules']:
#         print(j) 
#     print("correct Rules:")
#     for j in arr[i]['Spell']:
#         print(j) 
#     print("\n")


# [
#  ['दिग्गजवर', {'Correct_Rules': ['r2e'], 'Incorrect_Rules': ['r2f', 'r2c'], 'Result': 0, 'Spell':
# ['दिग्गज', 'किंग्जवर', 'ब्रिग्जवर', 'कटिंग्जवर', 'ड्रग्जवर']}],

#  ['दग्गजांत', {'Correct_Rules': ['r1a', 'r1b'], 'Incorrect_Rules': [], 'Result': 1, 'Spell': ['गजात', 'गजानंद', 'दिग्गजांबद्दल', 'दिग्गजांत', 'दिग्गजांसमवेत']}]
 
#  ]


from Spell_Checker import *
print(CheckSpell("अर्थसह")[0])

# ग्हण
# अर्थसह

 