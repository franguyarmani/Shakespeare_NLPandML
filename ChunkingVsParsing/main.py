from nltk.corpus import PlaintextCorpusReader
import nltk
from nltk.tag import pos_tag

import re
import string


#===================The Corpi======================
shakespeareRoot = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/ShakespeareCorpus"
plays = PlaintextCorpusReader(shakespeareRoot, '.*.txt')

harryPotterRoot = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/HarryPotterCorpus"
HP = PlaintextCorpusReader(harryPotterRoot, 'HarryPotterExcerpt.txt')

#==================Build Texts=====================

HamletRaw = plays.raw('Hamlet.txt')
DumbledoreRaw = HP.raw('HarryPotterExcerpt.txt')
#=================Extract Content===================
soliloquyStart = re.compile('To be, or not to be')
soliloquyEnd = re.compile('Be all my sins remember\'d\.')
Start = soliloquyStart.search(HamletRaw)
End = soliloquyEnd.search(HamletRaw)
soliloquy = HamletRaw[Start.start():End.end()]


quotelist = DumbledoreRaw.split('\"')[1::2] #creates a list of words split on 
                                            #quotation marks. Then selects the 
                                            # odd elements, which are the words 
                                            #between the quotes only. 
speech = " ".join(quotelist)                #joins the quoted text

#=================Count Sentences===================
sentEnders = re.compile('[.,?,:]')
soliloquySents = len(re.split('[.,?,:]', soliloquy))
speechSents = len(re.split('[.,?,:]', speech))

#=================Chunk Sentences==================
trees = []
grammar = "NP: {<DT>?<JJ>*<NN>}"
sentences = re.split('[.,?,:]', soliloquy)

for s in sentences[0:3]:
    noPunct =  s.translate(str.maketrans({}.fromkeys(string.punctuation)))
    print(noPunct)
    tagged = pos_tag(noPunct)
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tagged)
    print (result)



