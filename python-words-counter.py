# encoding: utf-8
#Marco Lorenzetti - programming with Python
#My first project carried out during my programming class at the University of Pisa

from operator import itemgetter

inFile=open(r"C:\Users\marco\Desktop\term-occurencies\cappuccettorosso.txt")
text=inFile.read()
inFile.close()

def filter_words(words):
	return [w for w in words if len(w)>3] #a rough stopwords funcition

parole=text.split()
filtered=filter_words(parole)
diz={}

for strings in (filtered):
        if strings not in diz:
                diz[strings]=1
        else:
                diz[strings]=diz[strings]+1
                
# 'itemgetter' was used according to the suggestions given here:
# http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python

print("-----------------------------------------------------------------------------------------------------------")
print("The first ten words:")
asc =sorted(diz, key=diz.get, reverse=True)
print(asc[:10]) #It means get or invoke all the dictionary key-value pairs in ascending order.

print("Treir frequency:")
frequencies=sorted(diz.items(),key=itemgetter(1),reverse=True)
print(frequencies[:10]) # It means get the key-value pairs based on the value and order them as a tuple list.
print("-----------------------------------------------------------------------------------------------------------")






