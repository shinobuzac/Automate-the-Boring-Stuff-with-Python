#! python3
# madlibs.py - read in text files and lets the user add their own text anywhere

import re

text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

repWordList = re.compile(r'[A-Z]{2,}').findall(text)
repList = []
for wordString in repWordList:
    if wordString[0].lower() == 'a':
        rep = input('Enter an %s\n' %wordString.lower())
    else:
        rep = input('Enter a %s\n' %wordString.lower())
    text = text.replace(wordString, rep, 1)
print(text)
open(r'C:\PY\madlibs.txt', 'w').write(text)
