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
import os

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

sceneBreak = re.compile('Scene|SCENE')

def cleanScenesC():
    path = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/Scenes"
    i = 0
    for play in comedies:
        listOfScenes = re.split(sceneBreak, play)
        for scene in listOfScenes:
            cleanScene = ' '.join(h.make_wordBank(scene))
            print(cleanScene)
            filename = "cScene" + str(i) + ".txt"
            f = open(os.path.join(path, filename), 'w')
            f.write(cleanScene)
            f.close
            print(i)
            i += 1

def cleanScenesT():
    path = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/Scenes"
    i = 0
    for play in tragedies:
        listOfScenes = re.split(sceneBreak, play)
        for scene in listOfScenes:
            cleanScene = ' '.join(h.make_wordBank(scene))
            print(cleanScene)
            filename = "tScene" + str(i) + ".txt"
            f = open(os.path.join(path, filename), 'w')
            f.write(cleanScene)
            f.close
            print(i)
            i += 1


cleanScenesC()
cleanScenesT()


