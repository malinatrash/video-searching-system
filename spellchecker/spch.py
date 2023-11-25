import spellchecker as spch
from time import time

spell = spch.SpellChecker("ru", local_dictionary="./ru.json.gz")
#text = input("Input sentence:\n").split()
text = "биува экстрасенсов".split()

start = time()
for i,word in enumerate(text):
    corr = spell.correction(word)
    if (corr): text[i] = corr
stop = time()
print(stop - start)
text = ' '.join(text)
print(text)

