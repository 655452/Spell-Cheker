from flask import Flask, jsonify, render_template,request
from flask_restful import Api, Resource, reqparse
from optim_gram import *
from grammar_rules import *
from Spell_Checker import *


app = Flask(__name__)
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

@app.route("/foo",methods=['POST'])
def foo():
    data=request.form['Word']
    payload={"Word":data}
    response=requests.post(BASE+"parse_word",json=payload)
    obj=response.json()
    # print(response.json())
    print(obj['Correct_Rules'])
    return render_template("Dummy.html",more=obj)

# final code


if __name__ == "__main__":
    app.run(debug=True ,port=8001)
