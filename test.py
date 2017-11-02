import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/ShakespeareCorpus"
plays = PlaintextCorpusReader(corpus_root, '.*.txt')

asYouLikeIt = plays.words('AsYouLikeIt.txt')

print(asYouLikeIt[0:20])
