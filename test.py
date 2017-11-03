
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import WordPunctTokenizer
import CleaningFunctions as c
import re

brackets = ["AsYouLikeIt.txt", "Hamlet.txt", "TamingOfTheShrew.txt", "TwelthNight.txt"]
CapNames = ["AsYouLikeIt.txt", "TamingOfTheShrew.txt", "TwelthNight.txt"]
SpacedDirections = []



corpus_root = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/ShakespeareCorpus"
plays = PlaintextCorpusReader(corpus_root, '.*.txt')

asYouLikeItRaw = plays.raw('AsYouLikeIt.txt')

asYouLikeItTokens = WordPunctTokenizer().tokenize(asYouLikeItRaw)

def remove_directions_space(rawText):
    #use a regular expresison to find space before and return after


print(c.remove_directions_brackets(asYouLikeItRaw)[:400])
#AYLITokensNoNames = (c.remove_all_caps(asYouLikeItTokens))
#print(c.remove_punctandnums(AYLITokensNoNames)[0:20])