
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer as l
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
MuchAdoAboutNothingRaw = plays.raw('MuchAdoAboutNothing.txt')
OthelloRaw = plays.raw('Othello.txt')
TamingOfTheShrewRaw = plays.raw("TamingOfTheShrew.txt")
TwelthNightRaw = plays.raw("TwelthNight.txt")

#==================Text Distictions===================

capNames = [AsYouLikeItRaw, CaesarRaw,TamingOfTheShrewRaw, TwelthNightRaw]
tragedies = [CaesarRaw, HamletRaw, KingLearRaw, MacbethRaw, OthelloRaw]
Comedies = [AsYouLikeItRaw, MuchAdoAboutNothingRaw, TamingOfTheShrewRaw, TwelthNightRaw]

clean = h.cleaner(KingLearRaw)
print(h.remove_nouns(clean))




#raw clean

#tokenize

#list clean

#lemmatize list

#remove nouns
