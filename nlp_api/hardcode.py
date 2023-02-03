###########################################
import pandas as pd
import numpy as np


##########################################

rule_db1 = {"क्ऱ्म": "क्रम", "रक्त": "रक्त",
            "समाप्त": "समाप्त", "खड्ग": "खडग्",
            "बूद्धी": "बुद्धी", "आशीर्वाद": "आर्शीवाद", "पन्ती": "पत्नी",
            "मुद्दाम": "मुददाम"}

# word = "माऊली"


def fetch_db():
    db = pd.read_csv("ww.csv")
    db = db.drop_duplicates()
    crct = db["Correct"]
    incrct = db["Incorrect"]
    incrct.index = crct
    db_dict = incrct.to_dict()
    return db_dict


def AA1(word):
    word = word.strip()
    # print(word)
    # print(rule_db1)
    if word in rule_db1.keys():
        return [True, rule_db1.get(word)]
    else:
        return [False, "Not in Db"]


def db_dict_word(word):
    db_dict_f = fetch_db()
    word = word.strip()
    print(word)
    for key, value in db_dict_f.items():
        # print(type(value))
        if type(value) != float:
            # print(key, value)
            if value.strip() == word:
                return [False, key]
            elif key.strip() == word:
                return [True, key]
    return [False, None]




