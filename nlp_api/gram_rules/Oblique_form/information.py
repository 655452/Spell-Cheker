'''It contains all the information regarding the project

---------------------------------------OVERVIEW OF PROGRAM----------------------------------------------------
main.py - contains the main code of the Program
adnaav.py - contains the code for Surnames
dataset.py - contains the list and dictionary of requried suffies, gramnaam, adnaav and exceptions
exception.py - contains the code for exceptions
gramnaam.py - contains the code for Gramnaam
oblique_form_rules.py - contains the code for the oblique form rules
suffixfunc.py - contains the code for finding suffi in the input word
verb_dataset - contains a dictionary of verbs
verb.py - contains the code for verb

----------------------------------------------OBLIQUE FORM RULES-------------------------------------------------

Rule 1.1 - Masculine word ending with Akarant (अकारान्त ) is converted to AAkarant(आकारांत)

Rule 1.2 - Masculine word ending with AAkarant(आकारांत) is converted to YAkarant (याकारांत)

Rule 1.3 - Masculine word ending with EEkarant (ईकरांत) is converted to YAkarant (याकारांत)

Rule 1.4 - Masculine word ending with UUkarant (ऊकारांत) is converted to VAkarant(वाकारांत)

Rule 1.5 - Masculine word ending with Ookarant (ओकारान्त) remains the same 

Rule 2.1(a) -  Feminine word ending with Akarant (अकारान्त) in Singular is converted to Aekarant (एकरांत)

Rule 2.1(a) - Feminine word ending with Akarant (अकारान्त) in Plural is converted to AAkarant(आकारांत)

Rule 2.1 (b) - Feminine word ending with Akarant (अकारान्त) in Singular and Plural is converted to EEkarant (ईकरांत)

Rule 2.2 -  Feminine word ending with AAkarant (आकारांत) in Singular is converted to Aekarant (एकरांत)

Rule 2.2 -  Feminine word ending with AAkarant (आकारांत) in Plural is converted by appending Anuswar (अनुस्वार) at the end

Rule 2.3 - Feminine word ending with EEkarant (ईकरांत) in Singular is converted to EEkarant (ईकरांत)

Rule 2.3 - Feminine word ending with EEkarnat (ईकरांत) in Plural is converted to YAkarant (याकारांत)

Rule 2.4 - Feminine word ending with UUkarant (ऊकारांत) in Singular is converted to Aekarant (एकरांत)

Rule 2.4 - Feminine word ending with UUkarant (ऊकारांत) in Plural is converted to VAkarant (वाकारांत)

Rule 2.5 - Feminine word ending with OOkarant (ओकारान्त) is not converted to Singular oblique form

Rule 2.5 - Feminine word ending with OOkarant (ओकारान्त) in Plural is converted to AAkarant (आकारांत)

Rule 3.1 - Neuter word ending with Akarant (अकारान्त) is converted to AAkarant(आकारांत)

Rule 3.2 - Neuter word ending with EEkarant (ईकरांत) is converted to YAkarant (याकारांत)

Rule 3.3 (a) - Neuter word ending with UUkarant (ऊकारांत) is converted to AAkarant(आकारांत)

Rule 3.3 (b) - Neuter word ending with UUkarant (ऊकारांत) is converted to VAkarant(वाकारांत)

Rule 3.4 - Neuter word ending with Aekarant (एकरांत) is converted to YAkarant (याकारांत)

Rule 4.1 - Surnames ending with Aekarant(एकरांत) are converted to YAkarant (याकारांत)

Rule 4.2 - Surnames ending with Akarant (अकारान्त) to AAkarant (आकारांत)

Rule 4.3 - Surnmaes ending with UUkarant (ऊकारांत) remains the same

Rule 4.4 - Surmanes ending with AAkarant (आकारांत) don't change

Rule 4.5 - Surnames ending with EEkarant (ईकरांत) don't change

Rule 5.1 - Gramnaam ending with AAkarant (आकारांत) is converted to YAkarant (याकारांत)

Rule 5.2 - Gramnaam ending with EEkarant (ईकरांत) remains the same

Rule 5.3 - Gramnaam ending with Aekarant (एकरांत) to YAkarant (याकारांत)

Rule 5.4 - Gramnaam ending with Akarant (अकारान्त) and having suffix - t (त) is converted to AAkarant (आकारांत)

Rule 5.4 - Gramnaam ending with Akarant (अकारान्त) and not having suffix - t (त) remains the same
'''