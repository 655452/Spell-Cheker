with open("final_dataframe.json", encoding='UTF-16') as F:
    import json
    data = json.load(F)
with open("Words.txt", "w", encoding='UTF-16') as F:
    L = data['words']
    for i in L:
        F.write(i + ",")

    