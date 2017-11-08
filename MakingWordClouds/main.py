from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer

import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud

from nltk.stem.wordnet import WordNetLemmatizer as l
from nltk.probability import FreqDist

import CleaningFunctions as c
import HelperFunctions as h
import re

#=====================The Corpus======================

corpus_root = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/ShakespeareCorpus"
plays = PlaintextCorpusReader(corpus_root, '.*.txt')

#=====================Build Texts=====================

AsYouLikeItRaw = plays.raw('AsYouLikeIt.txt')
CaesarRaw = plays.raw('Caesar.txt')
HamletRaw  =    plays.raw('Hamlet.txt')
KingLearRaw =  plays.raw('KingLear.txt')
MacbethRaw = plays.raw('Macbeth.txt')
MidsummerNightsDreamRaw = plays.raw('MidsummerNightsDream.txt')
MuchAdoAboutNothingRaw = plays.raw('MuchAdoAboutNothing.txt')
OthelloRaw = plays.raw('Othello.txt')
TamingOfTheShrewRaw = plays.raw("TamingOfTheShrew.txt")
TwelthNightRaw = plays.raw("TwelthNight.txt")

#==================Text Distinctions===================

capNames = [AsYouLikeItRaw, CaesarRaw,TamingOfTheShrewRaw, TwelthNightRaw]
tragedies = [CaesarRaw, HamletRaw, KingLearRaw, MacbethRaw, OthelloRaw]
comedies = [AsYouLikeItRaw, MidsummerNightsDreamRaw, MuchAdoAboutNothingRaw, TamingOfTheShrewRaw, TwelthNightRaw]
Undesirable = ["Caesar","thy","thee","thou"]


def tragedies_wordcloud():
    cleanText = ' '.join(h.make_wordBank(tragedies))
    wordCloud = WordCloud().generate(cleanText)
    print("cloud made")
    image = wordCloud.to_image()
    image.show()


def comedies_wordcloud():
    cleanText = ' '.join(h.make_wordBank(comedies))
    wordCloud = WordCloud().generate(cleanText)
    print("cloud made")
    image = wordCloud.to_image()
    image.show()

tragedies_wordcloud()
comedies_wordcloud()



    
    







#raw clean

#tokenize
#list clean
#lemmatize list
#remove nouns
#append text
