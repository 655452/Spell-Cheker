# main code
from suffixfunc import *
from exception import *
from gramnam import *
from adnaav import *
from verb import *
from oblique_form_rules import *

# take word as input from user
input_word = input("Enter your word:")
input_word = input_word.strip()

# list to store output
output = []

# check for suffix
stem_word, suffix = issuffix(input_word)
#print ("Stem word : ", stem_word,"\n Suffix:",suffix)


def output():
    # check for Exception
    output, flag = isException(input_word, stem_word, suffix)
    if(flag):
        return output

    else:
        # check for Gramnaam
        output, flag = isGramnam(input_word, stem_word, suffix)
        if(flag):
            return output

        else:
            # check for Adnav
            output, flag = isAdnav(input_word, stem_word, suffix)
            if(flag):
                return(output)

            else:
                # check for verb
                output, flag = isVerb(input_word, stem_word, suffix)
                if(flag):
                    return(output)

                else:
                    # Oblique form rules
                    # last index of stem_word
                    e = stem_word[-1]
                    if(e == "ं"):
                        if (stem_word[-3] == "व" and stem_word[-2] == "ा"):
                            output = VAkarant2_4(
                                input_word, stem_word, suffix)  # rule2.4 plural
                            return(output)

                        elif(stem_word[-3] == "य" and stem_word[-2] == "ा"):
                            output = YAkarant2_3(
                                input_word, stem_word, suffix)  # rule2.3 plural
                            output = anuswar(input_word, stem_word,
                                             suffix)  # rule 2.2 plural
                            return(output)

                        elif(stem_word[-4] == "ि" and stem_word[-2] == "ा"):
                            # rule2.1(a) plural
                            output = AAkarant2_1a(
                                input_word, stem_word, suffix)
                            return(output)

                        elif(stem_word[-2] == "ा"):
                            output = anuswar(input_word, stem_word, suffix)
                            output = EEkarant2_1b(
                                input_word, stem_word, suffix)
                            output = OOkarant2_5(input_word, stem_word, suffix)
                            return(output)
                            # rule2.2 plural and rule 2.1(b) plural and rule 2.5 plural

                        elif(stem_word[-2] == "ी"):
                            stem_word = stem_word[:-1]
                            output = EEkarant(
                                input_word, stem_word, suffix)  # rule2.1(b)
                            return(output)

                    elif(e == "ी"):
                        if(input_word[-3] == "ी"):
                            output = EEkarant(
                                input_word, stem_word, suffix)  # rule2.1(b)
                            # rule2.3 singular
                            output = EEkarant2_3(input_word, stem_word, suffix)
                            return(output)

                        else:
                            output = EEkarant(
                                input_word, stem_word, suffix)  # rule2.1(b)
                            return(output)

                    elif(e == "े"):
                        if(stem_word[-2] == "व"):
                            # rule2.4 singular
                            output = Aekarant2_4(input_word, stem_word, suffix)
                            return(output)
                        else:
                            output = Aekarant(input_word, stem_word, suffix)
                            output = Aekarant2_2(input_word, stem_word, suffix)
                            # rule2.1(a) and rule2.2 singular
                            return(output)

                    elif(e == "ो"):
                        output = Ookarant(input_word, stem_word, suffix)
                        output = Ookarant2_5(input_word, stem_word, suffix)
                        # rule1.5 and rule2.5 singular
                        return(output)
                    elif(e == "ा"):
                        if(stem_word[-2] == "व"):
                            output = VAkarant(input_word, stem_word, suffix)
                            output = VAkarant3_3b(
                                input_word, stem_word, suffix)
                            # rule1.4 and rule3.3(b)
                            return(output)

                        elif(stem_word[-2] == "य" and stem_word[-3] == "्"):
                            output = YAkarant(input_word, stem_word, suffix)
                            output = YAkarant1_3(input_word, stem_word, suffix)
                            output = YAkarant3_2(input_word, stem_word, suffix)
                            output = YAkarant3_4(input_word, stem_word, suffix)
                            # rule1.2 and rule1.3 and rule 3.2 and rule3.4
                            return(output)

                        elif(stem_word[1] == "ु"):
                            output = AAkarant3_1(
                                input_word, stem_word, suffix)  # rule3.1
                            return(output)

                        else:
                            output = AAkarant(input_word, stem_word, suffix)
                            output = AAkarant3_3a(
                                input_word, stem_word, suffix)
                            output = AAkarant3_1(
                                input_word, stem_word, suffix)  # rule3.1
                            # rule1.1  and rule 3.3(a)
                            return(output)
                    else:
                        d = {}
                        d[input_word] = {}
                        d[input_word]["Root_word"] = stem_word
                        d[input_word]["Stem_word"] = stem_word
                        d[input_word]["Rule"] = "n/a"
                        d[input_word]["Gender"] = "n/a"
                        d[input_word]["Number"] = "n/a"
                        d[input_word]["Suffix"] = suffix
                        d[input_word]["Part_of_Speech"] = "n/a"
                        output.append(d)
                        return(output)
