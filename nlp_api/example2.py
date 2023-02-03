from flask import Flask, jsonify, render_template,request
from flask_restful import Api, Resource, reqparse
from optim_gram import *
from grammar_rules import *
from Spell_Checker import *

app=Flask(__name__)



@app.route('/',methods=['POST','GET'])
def Word_Parser():
    
    if(request.method=='POST'):
        word=request.form['Word']
        # Add=request.form['Add_D']
        # print(Add)
        textL=word.split()
        if(len(textL)<2):
            Word=CheckSpell(word)
            print(Word)
            return render_template("Dummy.html",word=Word,text=word)
        else:
            arr=[]
            error_words=[]
            error_all=[]
            for i in textL:

                if i in folist:
                    i=[1,i]   
                    arr.append(i)
                    error_words.append(i)
                    
                else:
                    error_all_words=CheckSpell(i)
                    error_all.append(error_all_words)
                    Temp=correctWord(i)
                    Temp=[2,Temp]
                    error_words.append(Temp)
                    i=[0,i]
                    arr.append(i)
            # print(error_all)
            return render_template("Dummy.html",text=arr,correctW=error_words,option_for_error=error_all)
    return render_template("Dummy.html")

def correctWord(word):
    OP=CheckSpell(word)
    return OP[0]
# for removing spaces in the string
def remove(word):
    return word.replace(" ","")
# for adding word into the dict
def add_d(Word):
 with open("Dict.txt","a", encoding='UTF-8') as F:
        F.write(Word + ",")


@app.route("/add_to_dict",methods=['POST','GET'])
def Add_to_dict():
    bol=0
    Add=request.form['Add_D']
    print(len(Add))
    textL=Add.split()
    if(len(textL)<2):
        Add=remove(Add)
        print(len(Add))
        if Add in folist:
            print("dont Add it")
        else:
            if len(Add)<1:
                print("dont Add empty")
            else:
                add_d(Add)
                bol=1
                
                print("Add it to the lsit")
        
    else:
        print("sorry")
    print(bol)
    return render_template("Dummy.html",boll=bol)
# word prediction
@app.route("/word_predict",methods=['POST','GET'])
def word_predict():
    Word=request.form['wordP']
    Word=remove(Word)
    Word=CheckSpell(Word)
    return render_template("Dummy.html",word=Word)

# import requests
# import json
# BASE="http://127.0.0.1:5000/"
# payload={"Word":"दिग्गजही"}
# response=requests.post(BASE+"parse_word",json=payload)
# obj=response.json()
# # print(response.json())
# print(obj['Correct_Rules'])

if __name__=="__main__":
    app.run(debug=True)


# Demo Sesion
# from Spell_Checker import *
# Text=" दिग्गजही दिग्गज्जांसोबत दिग्गजांसह दिग्गजांवर दिग्गजांत "

# TEXTL = Text.split()

# print(len(TEXTL))
# OP={}
# for i in TEXTL:
#     OP[i]=CheckSpell(i)
# # print(OP['दिग्गजही'])
# for key in OP:
#     print(OP[key][0])
# print(OP)

# {'दिग्गजही': ['दिग्गजही', 'दिग्गज', 'गजही', 'दिग्गजांवरील', 'दिग्गजांचीही'], 

# 'दिग्गज्जांसोबत': ['दिग्गज्जांसोबत', 'दिग्गजांसोबत', 'दिग्गजांसोबतची', 'दिग्गजांसो
# बतच्या', 'दिग्गजांत'], 
# 'दिग्गजांसह': ['दिग्गजांसह', 'दिग्गजांसमोर', 'दिग्गजांवर', 'दिग्गजांसमवेत', 'दिग्गजांत'], 'दिग्गजांवर': ['दिग्गजांवर', 'गजांवर', 'दिग्गज
# ांवरील', 'दिग्गजांसमोर', 'दिग्गजांसह'],
#  'दिग्गजांत': ['दिग्गजांत', 'दिग्गजांसोबत', 'दिग्गजांसह', 'दिग्गजांवर', 'दिग्गज्जांसोबत']}