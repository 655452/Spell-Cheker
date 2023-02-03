from gram_rules import basic_rule, advance_rule


def Return_Rules(text):
    correct_adv = []
    incorrect_adv = []

    correct_bas = []
    incorrect_bas = []

    adv_rules = advance_rule.word_input(text, correct_adv, incorrect_adv)
    bas_rules = basic_rule.word_input(text, correct_bas, incorrect_bas)

    correct = []
    incorrect = []
    correct = adv_rules[0][text]['correct'] + bas_rules[0][text]['correct']
    incorrect = adv_rules[0][text]['incorrect'] + \
        bas_rules[0][text]['incorrect']
    #####################################################
    ####### RULE WEIGHTAGE CALCULATION ########
    adv_corr_len = len(adv_rules[0][text]['correct'])
    adv_incorr_len = len(adv_rules[0][text]['incorrect'])
    bas_corr_len = len(bas_rules[0][text]['correct'])
    bas_incorr_len = len(bas_rules[0][text]['incorrect'])
    ######################################################
    cor = adv_corr_len + bas_corr_len
    incor = adv_incorr_len + bas_incorr_len
    # print(cor)
    if incor >= 2:
        if cor > incor:
            result = 1
        else:
            result = 0
    else:
        result = 1
    ######################################################
    return correct, incorrect, result

# print(Return_Rules("दिग्जही दिग्गज्जांसोबत दिग्गज्जांसोबत दिग्गज्जांसोबत दिग्गज्जांसोबत दिग्गज्जांसोबत"))

# द ि ग ् ज ह ी दिग्जही 

# द ि ग ् ग ज ह ी   द ि ग ् ग ज ् ज ा ं स ो ब त   द ि ग ् ग ज ा ं स ह   द ि ग ् ग ज ा ं व र   द ि ग
#  ् ग ज ा ं त दिग्गजही दिग्गज्जांसोबत दिग्गजांसह दिग्गजांवर दिग्गजांत
# (['UU16', 'r1b', 'r2e', 'r1c'], ['r2f', 'r2c'], 1)