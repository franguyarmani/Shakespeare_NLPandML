
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

#=====================The Corpus======================

corpus_root = "C:/Users/fbpea/Git_Repositories/Shakespeare_NLPandML/ShakespeareCorpus"
plays = PlaintextCorpusReader(corpus_root, '.*.txt')

#=====================Build Text=====================

sentences= plays.sents()

#====================

model = defaultdict(lambda: defaultdict(lambda: 0))
 
for sentence in sentences:
    for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
        model[w1][w2] += 1
 
 
# Let's transform the counts to probabilities
for w1 in model:
    total_count = float(sum(model[w1].values()))
    for w2 in model[w1]:
        model[w1][w2] /= total_count
