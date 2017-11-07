from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import WordPunctTokenizer

import re

import codecs


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


quotelist = DumbledoreRaw.split('\"')[1::2] #creates a list of words split on quotation marks. 
                                            #Then selects the odd elements, which are the words between the quotes only. 
speech = " ".join(quotelist)                #joins the quoted text

#==================Count Sentences===================
sentEnders = re.compile('[.,?,:]')
soliloquySents = len(re.split('[.,?,:]', soliloquy))
speechSents = len(speech.split('.'))
print(soliloquySents)





#print(HamletRaw[Start.start():End.end()])
