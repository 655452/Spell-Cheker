from get_Gram import showGrams
import json

def Get_Grams(a,b):
	a=a.strip()
	b=b.strip()

	fga,x,fgna,x=showGrams(a)
	fgb,x,x,x=showGrams(b)
	x=fgna
	fgna={}
	for k,v in x:
		fgna[k]=int(v)
	x=fgb
	fgb={}
	for k,v in x:
		fgb[k]=int(v)

	if a and b=="":     # -- means a is the first word and starting
		return fga
	elif a and b:
		a_keys=fgna.keys()
		b_keys=fgb.keys()
		c_bigrams={}
		mini="b" if len(a_keys)>len(b_keys) else "a"
		if mini=="a":
			for x in a_keys:
				if x in b_keys:
					c_bigrams[x]=fgna[x] if fgna[x]>fgb[x] else fgb[x]
		else:
			for x in b_keys:
				if x in a_keys:
					c_bigrams[x]=fgna[x] if fgna[x]>fgb[x] else fgb[x]
		return c_bigrams
	else:
		pass

# print(Get_Grams("दिग्गजांवर","दिग्गजांवर"))