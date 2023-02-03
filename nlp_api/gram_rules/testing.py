import advance_rule
import basic_rule
import json

text = ""


correct_bas = []
incorrect_bas = []
correct_adv = []
incorrect_adv = []
adv_json = {}
bas_json = {}
adv_rules = {}
bas_rules = {}

adv_rules = advance_rule.word_input(text, correct_adv, incorrect_adv)

bas_rules = basic_rule.word_input(text, correct_bas, incorrect_bas)

adv_json = json.dumps(adv_rules, indent=6, ensure_ascii=False)
bas_json = json.dumps(bas_rules, indent=6, ensure_ascii=False)

adv_corr_len = len(adv_rules[0][text]['correct'])
adv_incorr_len = len(adv_rules[0][text]['incorrect'])
bas_corr_len = len(bas_rules[0][text]['correct'])
bas_incorr_len = len(bas_rules[0][text]['incorrect'])

cor = adv_corr_len + bas_corr_len
incor = adv_incorr_len + bas_incorr_len

data_crct = bas_rules[0][text]['correct'] + \
    adv_rules[0][text]['correct']
data_incrct = bas_rules[0][text]['incorrect'] + \
    adv_rules[0][text]['incorrect']
if incor >= 2:
    if cor > incor:
        result = 1
    else:
        result = 0
else:
    result = 1
