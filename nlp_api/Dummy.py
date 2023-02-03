from flask import Flask, jsonify, render_template,request,after_this_request
from flask_restful import Api, Resource, reqparse
from optim_gram import *
from grammar_rules import *
from Spell_Checker import *

app=Flask(__name__)


api = Api(app)


# TEXT_PARSER takes a string or a single word as a argument and replies in format {word : [[font_color], [suggestions]]}
post_args = reqparse.RequestParser()
post_args.add_argument("Text", type=str, required=True)


class Text_Parser(Resource):
    def post(self):
        args = post_args.parse_args()
        TEXT = args['Text']
        TEXTL = list(TEXT.split())
        OP = {}
        for i in TEXTL:
            OP[i] = CheckSpell(i)
        return jsonify({"data":OP})


# Word Parser Takes a post word in json format as {'Word' : "Query Word"} and replies json as {"Correct_rules" : [], "Incorrect_Rules" : [], "Spell": [[Font Color], [Suggestions if any]]}
post_word = reqparse.RequestParser()
post_word.add_argument("Word", type=str, required=True)


class Word_Parser(Resource):
    def post(self):
        args = post_word.parse_args()
        Word = args['Word']
        Output = {}
        Output["Spell"] = CheckSpell(Word)
        Output["Correct_Rules"], Output["Incorrect_Rules"], Output["Result"] = Return_Rules(
            Word)

        return jsonify(Output)


# add_to_dict takes a json post as {"Add_Word" : Word to be added} and replies message if word added.
add_word = reqparse.RequestParser()
add_word.add_argument("Add_Word", type=str, required=True)


class Add_To_Dict(Resource):
    def post(self):
        args = add_word.parse_args()
        Add_To_Dictionary(args["Add_Word"])
        return jsonify({"message": "Word Added Successfully"})


# In this function we pass a json {"Word1": value, "Word2" : value} to the predicter and it responses as {"Suggestions" : [values]}
predict_word = reqparse.RequestParser()
predict_word.add_argument("Word1", type=str, required=True)
predict_word.add_argument("Word2", type=str, required=False)


class Predict_Word(Resource):
    def post(self):
        args = predict_word.parse_args()
        Out = Get_Grams(args["Word1"], args["Word2"])
        Out = list(Out.keys())
        return jsonify({"Suggestions": Out})


api.add_resource(Text_Parser, "/parse_text")
api.add_resource(Word_Parser, "/parse_word")
api.add_resource(Add_To_Dict, "/add_word")
api.add_resource(Predict_Word, "/predict_grams")


import requests
import json
BASE="http://127.0.0.1:5000/"

@app.route("/foo",methods=['GET','POST'])
def foo():
    if(request.method=='POST'):
        data=request.form['Rules']
        payload={"Word":data}
        response=requests.post(BASE+"parse_word",json=payload)
        obj=response.json()
        # print(response.json())
        print(obj['Correct_Rules'])
        return render_template("index.html",Rule=obj)
    else:
        return render_template("index.html")


@app.route('/',methods=['POST','GET'])
def Word_correction():
    
  
    return render_template("index.html")

# def createObject(obj):


def correctWord(word):
    OP=CheckSpell(word)
    return OP[0]   #this is for corrected word
    # return word
# for removing spaces in the string
def remove(word):
    return word.replace(" ","")
# for adding word into the dict
def add_d(Word):
 with open("Dict.txt","a", encoding='UTF-8') as F:
        F.write(Word + ",")


@app.route("/add_to_dict",methods=['POST','GET'])
def Add_to_dictionary():
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
    return render_template("index.html",boll=bol)
# word prediction
@app.route("/word_predict",methods=['POST','GET'])
def word_predict():
    Word=request.form['wordP']
    Word=remove(Word)
    Word=CheckSpell(Word)
    return render_template("index.html",word=Word)
#  for sample purpose
# import flask import after_this_request
@app.route("/new/<name>",methods=['POST','GET'])
def newpredict(name):
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin',"*")
        return response
    Word=name
    Word=remove(Word)
    Word=CheckSpell(Word)
    return jsonify(Word)

# parse text
@app.route("/text_parse",methods=['POST','GET'])
def textParser():
     if(request.method=='POST'):
        text=request.form['Word']
        print(text)
        # Add=request.form['Add_D']
        # print(Add)
        error_data=[]
        actual_data=[]
        textL=text.split()
        for i in textL:
            if(len(textL)>1):
                if i in folist:
                    temp=[0,i]
                    actual_data.append(temp)
                else:
                    
                    payload={"Word":i}
                    response=requests.post(BASE+"parse_word",json=payload)
                    obj=response.json()
                    temp=[1,i,obj]
                    actual_data.append(temp)
                    obj=[i,obj]
                    
                    error_data.append(obj)

                    # print(response.json())
                

# for getting rules and suggestion fof words
        
        # textL=word.split()
        print(actual_data)
        # print(error_data)
        return render_template("index.html",actualD=actual_data,errorD=error_data)
     return render_template("index.html")


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
