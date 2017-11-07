from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import WordPunctTokenizer

import re


#===================The Corpi======================
shakespeareRoot = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/ShakespeareCorpus"
plays = PlaintextCorpusReader(shakespeareRoot, '.*.txt')

harryPotterRoot = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/HarryPotterCorpus"
HP = PlaintextCorpusReader(harryPotterRoot, 'HarryPotterExcerpt.txt')

#==================Build Texts=====================

HamletRaw = plays.raw('Hamlet.txt')
DumbledoreRaw = HP.raw('HarryPotterExcerpt.txt')
#=================Extract Content===================
re.DOTALL
soliloquyStart = re.compile('To be, or not to be')
soliloquyEnd = re.compile('Be all my sins remember\'d\.')
Start = soliloquyStart.search(HamletRaw)
End = soliloquyEnd.search(HamletRaw)

print(HamletRaw[Start.start():End.end()])
