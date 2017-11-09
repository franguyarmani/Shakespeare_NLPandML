from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import nltk

from nltk import Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk.draw.tree import TreeView

import os


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
grammar = """ 
    S: {<NP><VP>} 
    NP: {<DT>?<JJ>*<NN>}
        {<DT>?<JJ>*<PRP>}
        {<DT>?<JJ>*<NNP>}
        {<DT>?<JJ>*<NNS>}
    PP: {<P><NP>}
    VP: {<VB><NP>|<VP><PP>}
    IF: {<TO><VB>}
"""
sentences = re.split('[.?:]', speech)


first3 = sentences[0:3]
#print (first3)


for s in first3:
    noPunct = s.translate(str.maketrans({}.fromkeys(string.punctuation)))
    #print(noPunct)
    s = "The little yellow dog ran across the street"
    text = word_tokenize(noPunct)
    tagged = pos_tag(text)
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tagged)
    TreeView(result)

    







